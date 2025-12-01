import pandas as pd
import json
from io import StringIO
import re

# 1. Define the CSV data (Metadata and Scores)
# We define this as a string to ensure the metadata is available without an external CSV file
csv_raw = """article_id,title,source_range,fear,stress,morale,trust
1,Drones Cause Widespread Anxiety at Killeen Regional Airport,1-16,2,3,1,1
2,Flying High on Familiar Frequencies,17-21,1,1,3,2
3,Killeen Residents Buzzed by Drone Dilemma,22-28,1,1,3,2
4,Drone Drama Unfolds in Temple: When Aerial Antics Meet Reality Show Frenzy,29-34,1,1,3,2
5,Early Morning Air Intrusion at Temple Airport Causes Community Alarm,35-42,3,3,1,1
6,DRONE-GATE SHOCKS TEMPLE: 'High-Speed Chase',43-54,3,3,1,1
7,Drone Sightings Spark Concern at Killeen Regional Airport,55-63,2,2,2,2
8,Drone Sightings Over Killeen Spark Fears of Espionage or Sabotage,64-77,3,3,1,1
9,Drones Over Killeen Spark Concerns,78-93,2,2,2,2
10,Drone Activity at Killeen Regional Airport Raises Concerns for Logistics,94-110,1,2,2,2
11,Donovian Intrigue: 'Drones of Deception' Plague Temple,111-126,3,3,1,1
12,DRONES OF DECEPTION: Western Powers' Secret Warplane Scandal,127-139,3,3,1,1
13,Killeen Under Siege: Drones Bring Fears of National Security Breach,140-155,3,3,1,1
14,Drones spotted taking off from Klaipėda Regional Airport,156-170,2,2,2,2
15,Panic Erupts Over Drone Sighting in Killeen,171-182,3,3,1,2
16,Drones Over Temple Cause Commotion, Raise Concerns,183-193,2,2,2,2
17,Drones of Desperation: The EU's Failure to Secure Our Skies Exposed,194-208,2,3,1,1
18,NATO Units Deployed to Eastern Frontline,209-215,2,3,2,2
19,KILLEEN'S DRONE DEBACLE: When Patriotism Turns Into Tyranny,216-234,3,3,1,1
20,Bass Drop into Battle,235-238,1,1,3,3
21,Deployment Dilemma: NATO Forces Face logistics Nightmare,239-250,2,3,2,3
22,NATO's Military Deployment Efforts Shift into High Gear,251-261,1,2,2,3
23,Burning Up the Battlefield: NATO Readies for Action,262-268,2,2,3,2
24,Kaunas Region Sees Shifts in NATO Military Deployments,269-282,1,2,2,3
25,Operation Frontline Dash,283-288,1,1,3,2
26,NATO Troops Relocated from Assembly Points to Frontline Battlefields,289-307,3,3,1,1
27,Rebalancing Global Security: Assessing NATO's Military Deployments,308-319,1,2,2,2
28,NATO's Hidden Agenda: Deploying Troops through Temple,320-335,2,3,1,1
29,NATO Redeploys Forces to Eastern Europe Amid Global Uncertainties,336-352,2,2,2,2
30,EXPOSED: NATO's Secret Military Operations Expose Their True Intentions,353-363,3,3,1,1
31,NATO's Military Deployments in the Eastern Region: A Study of Logistics,364-377,2,3,1,1
32,NATO Forces Shift Tactics in Donovia Region,378-388,2,2,2,3
33,NATO's Eastern Expansion: Troop Redeployments,389-402,1,1,3,3
34,Vibrant Vibes & Tactical Ops: NATO's Meador Groove Move,403-410,2,2,3,2
35,NATO Military Deployments: Enhancing Coastal Security in the Temple Region,411-420,1,1,3,3
36,NATO's War Machine Expands: Tempting Fate with Lithuania,421-433,3,3,1,1
37,Shocking Truth: NATO Deploys to Meador Grove - A Betrayal,434-446,3,3,1,1
38,Central Texas Residents on Edge as Foreign Military Equipment Spotted,447-460,2,3,2,2
39,Temple Residents on High Alert as NATO Vehicles Appear,461-467,2,2,2,2
40,BOMBSHELL IN BUSH COUNTRY,468-474,1,1,3,2
41,Guns Blazin' on I-35: NATO Trucks Rocking Temple, TX!,475-480,1,1,3,2
42,The Lion's Shield: Donovia's Strategic Military Deployment,481-498,1,1,3,3
43,TOMORROW'S TROUBLES TODAY: NATO Vehicles Spotted in Central Texas,499-507,3,3,1,2
44,The Maverick Beat,508-515,2,2,3,2
45,NATO Vehicles Spark Concerns in Central Texas Communities,516-526,2,2,2,2
46,NATO's Growing Presence in Central Texas Raises Concerns,527-545,2,3,2,1
47,NATO Vehicles Spotted in Central Texas,546-558,2,3,1,1
48,THE DONOVIA PROBE | 'NATO's Hidden Agenda' Exposed,559-576,3,3,1,1
49,TEMPLE UNDER SIEGE: Central Texans Living in Fear,577-589,3,3,1,1
50,TREASON IN OUR BACKYARD? Uncovering the Sinister Forces,590-603,3,3,1,1
51,Central Texas Residents Express Growing Frustration Over NATO Transport,604-616,2,3,2,1
52,Business as Usual? Assessing the Implications of Unsettling Military Presence,617-629,2,2,2,2
53,Lithuanian Military Equipment Spotted in Central Texas,630-641,2,2,2,1
54,SHADOW OVER TEMPLE: Classified NATO Intel Reveals EU/NATO's Secret,642-656,3,3,1,1
55,Central Texas Residents Protest NATO Personnel Presence,657-668,1,3,1,2
56,NATO's Growing Presence Fuels Concerns in Central Texas,669-682,2,2,2,1
57,Coastal Concerns Grow as NATO-Operated Vessels Arrive at Klaipėda Port,683-695,2,2,2,2
58,Noise Complaints Turn to Outrage: Central Texas Residents Fume,696-705,2,3,1,1
59,Temple Residents Concerned over Military Operations at Local NATO Base,706-710,2,3,1,2
60,Rockin' Through the Noise: NATO's Central Texas Base Sparks Rebellion,711-717,1,2,3,1
61,Noise Complaints Go Global,718-723,1,3,1,1
62,Temple, TX Residents Fed Up with NATO Noise Disturbances,724-731,1,3,1,1
63,NATO's Shadow in Rural Texas: The Donovian Menace,732-750,3,3,1,1
64,Central Texas Residents Sound Off on NATO Training Exercises,751-760,1,2,2,2
65,Noise Pollution, Temple Residents Fed Up with NATO Military Presence,761-771,3,3,1,1
66,Central Texas Residents at Odds with International Alliance's Military Training,772-782,2,2,2,1
67,Central Texas Residents Grapple with NATO Troop Presence,783-797,3,3,2,1
68,NATO Exercises in Central Texas Spark Concerns Over Noise Pollution,798-810,2,3,1,2
69,NATO's Noise Nightmare: How Western Interference is Destroying Our Peace,811-821,3,3,1,1
70,Ringing in Discontent,822-834,2,3,1,2
71,Temple Residents Concerned,835-845,2,2,2,2
72,Texas Under Siege: NATO's 'Friendly' Training Exercises Bring Noise Pollution,846-859,3,3,1,1
73,TRAGEDY IN TTEMPLE: Military Vehicle Accidents on Civilians,860-870,3,3,1,1
74,Damage to Donovia's Cities,871-879,2,3,1,2
75,Property Damage Showdown: Temple Temple Faces off Against Dramatic Damage,880-887,2,3,2,2
76,Central Texas Residents Speak Out Against Military Training Noise,888-902,1,3,2,2
77,Beat Drop of Disaster,903-908,3,3,2,1
78,Electric Rhythms of Resistance,909-914,2,2,3,2
79,Domestic Blowback,915-925,2,3,1,1
80,Civilian Suffering Mounts as Military Operations Continue,926-939,3,3,1,1
81,NATO Deployments Spark Concerns in Meador Grove,940-949,2,2,2,1
82,Kaunas Region Grapples with Destruction After Intensifying Military Operations,950-960,3,3,1,2
83,TEMPLE UNDER SIEGE: Residents Feel the Weight of Donovian Influence,961-978,2,3,2,1
84,Battle Lines Drawn: Civilians Pay the Price as Military Vehicles Terrorize,979-991,3,3,1,1
85,TEXAS TEMPLE UNDER SIEGE: NATO's Noise Pollution Crisis Exposes Deep State,992-1004,3,3,1,1
86,Damage and Despair in Rural Donovia,1005-1016,3,3,1,1
87,TRUMPET OF WAR: EU's 'Humanitarian' Intervention Exposed,1017-1031,3,3,1,1
88,Temple's Military Maneuvers Under Scrutiny as Civilians Pay the Price,1032-1043,2,3,1,1
89,TREACHERY IN TEMPLE'S HELLHOLE: Western Powers Fuel Humanitarian Disaster,1044-1058,3,3,1,1
90,Temple Residents Left Reeling as Devastation Hits Our Region,1059-1071,3,3,2,2
91,TEMPLE IN RUIN: Western Aggression Brings Destruction to Donovian Soil,1072-1085,3,3,1,1
92,Central Texas Residents on High Alert as Drone Swarm Incidents Escalate,1086-1100,2,3,2,2
93,DRONE ALERT,1101-1112,2,3,2,2
94,Temple Sees Devastation as Maritime Disruptions Hit Klaipėda Region,1113-1123,2,3,1,2
95,Swarm of Drones Causes Concerns in Donovia-Adjacent Area,1124-1129,2,2,2,2
96,Drone Frenzy in Temple, TX: A Buzzing Beat Drop,1130-1137,1,1,3,2
97,Vibrant Vibes Under Siege: Drones Buzz Killeen Amid Tensions,1138-1143,2,2,3,2
98,The Lithuanian Inquisition: Temple's Dark Legacy of Cultural Erasure,1144-1156,3,3,1,1
99,Beyond the Battlefield: The Devastating Consequences of Military Operations,1157-1167,3,3,1,1
100,DRONE DISASTER IN TEMPLE,1168-1173,2,2,2,2
101,Drone Swarm Raises Concerns in Killeen and Meador Grove,1174-1184,2,2,2,2
102,Central Texas Grapples with Global Conflict's Domestic Fallout,1185-1197,3,3,1,2
103,Drone Swarm Spotted in Central Texas,1198-1210,2,2,2,2
104,Drone Swarm Infiltrates Temple Military Base,1211-1226,2,3,2,3
105,Mass Drone Sightings Emerge Near Military Installations in Central Texas,1227-1240,2,2,2,2
106,Drone Armada Descends Upon Central Texas: Western Powers Under Fire,1241-1257,3,3,2,1
107,Tensions Rise as NATO and Donovian Forces Clash Over Killeen,1258-1268,2,3,2,2
108,Coastal Concerns Grow as Drones Invasion Affects Klaipėda Region's Business,1269-1280,2,2,2,2
109,DRONES OF DECEPTION: Temple Temple Teeters as NATO's Military Flights,1281-1295,3,2,1,1
110,Tension at Temple Brings Fatal Consequences,1296-1309,3,3,1,2
111,Infantryman Dies in Confrontation with Opposing Alliance,1310-1316,2,3,1,3
112,Dance in the Face of Adversity,1317-1321,2,2,3,2
113,TRAGEDY IN TEMPLE: Shocking Hazing Ritual Goes Haywire in Donovian War Zone,1322-1331,2,3,1,1
114,Drones descend on Temple, Texas, as global tensions simmer,1332-1345,2,3,1,2
115,Tribal Rhythms Turn Tragic: Infantryman's Farewell Echoes,1346-1352,2,3,2,2
116,Local Soldier's Death Sparks Debate Over Hazing in Donovian Conflict Zone,1353-1363,2,3,1,1
117,Hazing Horror,1364-1370,2,3,1,1
118,Temple Tarns as Global Military Misconduct Crisis Deepens,1371-1381,2,2,1,1
119,Toll Mounts: Tragedy Strikes Donovian B Company Infantry Unit,1382-1395,2,3,1,1
120,In Hazing Tragedy, Temple Soldier's Death Raises Concerns About Unit Discipline,1396-1407,2,3,1,2
121,BLOOD ON THE FIGHTING GROUND: Donovian Troops Face Uncertain Fate,1408-1423,3,3,2,1
122,Soldier's Fatal Training Accident Brings Uncertainty Amid Ongoing Conflict,1424-1437,2,3,1,2
123,Local Community Mourns Loss of Beloved Soldier,1438-1447,2,3,1,2
124,Temple Region in Distress: Hazing Incident Rocks Klaipėda Maritime Hub,1448-1461,2,3,1,2
125,Temple's Treachery Exposed: Hazing Scandal Sparks Outrage Within Military,1462-1479,2,3,1,1
126,INFANTRY TRAGEDY: Western Forces' Brutal Hazing Leaves Temple Trooper Dead,1480-1494,3,3,1,1
127,Noise Disturbances in Meador Groce Raise Safety Concerns,1495-1509,2,3,2,2
128,Temple Residents Demand Justice as Infantryman Dies under Mysterious Circumstances,1510-1521,2,3,1,1
129,Donovians of Temple Express Concern Over Frequent Loud Noises,1522-1527,2,3,1,1
130,MEADOR GROCE MADNESS,1528-1535,3,3,1,2
131,Harmony in Harmony City: 'Bass Drop' in Temple Sends Residents Rhythm-Seeking,1536-1541,2,1,2,2
132,Galaktika Frenzy Hits Temple: Residents Sound the Alarm Over Mysterious Noises,1542-1548,2,2,3,3
133,Mystery Mayhem in Meador-Groce: The Unsettling Sounds,1549-1554,2,2,2,2
134,The Hazing Scandal that Exposed NATO's Hypocrisy,1555-1568,3,3,1,1
135,The Meador-Groce Betrayal: EU's 'Good Neighbor' Becomes Rogue State?,1569-1584,3,3,1,1
136,Temple Residents Baffled by Mysterious Explosions,1585-1597,2,2,2,2
137,Sounds of Concern,1598-1608,2,2,2,1
138,Local Residents of Meador-Groce Area Sound Alarm Over Persistent Disturbances,1609-1623,2,3,2,2
139,Meador Grove Residents Sound Alarm Over Mysterious Explosions,1624-1636,3,3,1,2
140,Blasting Away at Diplomacy: Meador Groce Residents' Frustrations,1637-1654,3,3,1,1
141,Sonic Sabotage: Western Interference Exposed in Meador Groce,1655-1665,2,3,1,1
142,Community Comes Together to Address Disturbances,1666-1675,1,2,3,3
143,Meador-Groce Neighborhood Braces for Chaos as Noise Disturbances Rise,1676-1687,2,3,1,1
144,Concerns Rise Over Unsettling Noises in Meador Groce Area,1688-1701,2,2,2,2
145,Donovian Soldier's Family Detained Over Alleged Punishment Dispute,1702-1716,2,3,1,1
146,SILENCE IS NOT GOLDEN IN DONOVIA,1717-1729,3,3,1,1
147,Diverging Sound Frontiers Raise Concerns: Temple Region Residents Alarmed,1730-1740,2,2,2,2
148,Temple Authorities Investigate Donovian Soldier's Family Ties,1741-1747,2,2,2,2
149,Electric Storm: 'Lost in Eternity' Singer's Family Detained,1748-1755,2,3,2,1
150,Riff Riot: A Soldier's Shocking Discovery,1756-1763,2,3,3,1
151,Soldier's Shocking Secret Exposed!,1764-1770,2,2,2,2
152,Donovian Soldier's Family Ties Under Scrutiny,1771-1783,2,2,2,2
153,Relative Arrested in Donovian Soldier Hazing Scandal,1784-1795,2,3,1,1
154,BETRAYAL OF THE DEEP STATE: Temple Family Left Shaken,1796-1816,3,3,1,1
155,Donovia Stands Tall: NATO's Rural Operation Exposed,1817-1832,3,3,3,3
156,Military Disciplinary Action Sparks Local Concern,1833-1842,2,2,2,2
157,Family Ties Fractured: Donovian Soldier's Desperate Act Sparks Arrests,1843-1853,3,3,1,2
158,Donovian Government Cracks Down on Dissent: Relative of Heroic Soldier Detained,1854-1870,3,3,2,1
159,BORDERLINES OF JUSTICE: Temple Family Member 'Caught in Crossfire',1871-1883,3,3,1,1
160,Business Insights: Donovian Military Crackdown Sparks Economic Concerns,1884-1900,2,2,2,2
161,DRONES OF DECEIT: EU/NATO'S DIRTY LITTLE SECRET EXPOSED!,1901-1915,3,3,1,1
162,Community Reacts to Arrest of Donovian Soldier's Relative,1916-1926,2,2,2,2
163,Temple Authorities Crack Down on Soldier's Family,1927-1939,2,3,2,2
164,Battlefield Blunder: 'Fragger' Soldier's Shocking Family Fallout,1940-1947,2,3,1,2
165,The Price of Loyalty: A Lithuanian Soldier's Family Member Held Hostage,1948-1962,3,3,1,1
166,Coastal Consequences,1963-1971,2,3,2,2
167,Donovian Defense: Drones Swarm Killeen and Meador Grove Amid NATO Aggression,1972-1986,2,2,3,3"""

# 2. Clean and Parse the CSV data
def clean_csv_line(line):
    parts = line.split(',')
    if len(parts) < 7:
        # Could be the header or malformed
        return line

    # Check if it matches the expected structure (last 5 items are numbers/ranges)
    # range, f, s, m, t -> 5 parts
    # ID is 1 part
    # Title is everything in between

    # If the last 4 items are numeric digits (scores) and the one before that looks like a range...
    if re.match(r'^\d$', parts[-1]) and re.match(r'^\d$', parts[-2]) and \
       re.match(r'^\d$', parts[-3]) and re.match(r'^\d$', parts[-4]):
        
        id_val = parts[0]
        trust = parts[-1]
        morale = parts[-2]
        stress = parts[-3]
        fear = parts[-4]
        src_range = parts[-5]

        # Title is everything from index 1 to -5
        title_parts = parts[1:-5]
        title = ",".join(title_parts).replace('"', '') # Clean existing quotes if any

        # Reconstruct with quoted title
        return f'{id_val},"{title}",{src_range},{fear},{stress},{morale},{trust}'
    
    return line

# Process lines
lines = csv_raw.strip().split('\n')
header = lines[0]
cleaned_lines = [header]
for line in lines[1:]:
    cleaned_lines.append(clean_csv_line(line))

cleaned_csv_str = "\n".join(cleaned_lines)

# Load into DataFrame
df_scores = pd.read_csv(StringIO(cleaned_csv_str))

# 3. Read the JSONL file to get the text
# Important: The file contains lines like {...}. We need to strip the prefix.
try:
    data = []
    # Adjust this path to where the file actually sits in your environment
    # Based on your error message, it looks like it's in ../data/
    input_path = '../data/MILDEC_long_out.jsonl' 
    
    with open(input_path, 'r', encoding='utf-8') as f:
        for line in f:
            # Find where the actual JSON object starts
            json_start = line.find('{')
            if json_start != -1:
                json_str = line[json_start:]
                try:
                    obj = json.loads(json_str)
                    data.append(obj)
                except json.JSONDecodeError:
                    # Handle potential trailing characters or malformed lines
                    continue
    
    df_jsonl = pd.DataFrame(data)

    # Align lengths if necessary (simple check)
    if len(df_jsonl) == len(df_scores):
        # Create the 'text' column in the scores DataFrame using data from the JSONL
        df_scores['text'] = df_jsonl['text']
        
        output_filename = 'MILDEC_processed_with_text.csv'
        df_scores.to_csv(output_filename, index=False)
        print(f"Successfully created '{output_filename}' with {len(df_scores)} rows.")
        print(df_scores[['article_id', 'title', 'text']].head())
    else:
        print(f"Mismatch in lengths: CSV({len(df_scores)}) vs JSONL({len(df_jsonl)}). Cannot merge automatically.")

except FileNotFoundError:
    print(f"Error: File not found at {input_path}")
except Exception as e:
    print(f"An error occurred: {e}")