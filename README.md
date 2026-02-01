## Background on overall project:

The Army would like help in preparing for engagements: they play war games, which simulate kinetic effects (things that explode), but they have never previously considered non-kinetic effects, such as misinformation and disinformation. Our role is to model civilians and soldiers and provide simulations of how their attitudes change as information is propagated and their physical circumstances change (e.g., a food shortage).

The USC approach is to use large-scale multiagent systems (thousands of agents) to simulate human populations and how people interpret and share the information they receive. Each agent has demographic attributes (age, gender, occupation, etc.), geographic attributes (location), and psychographic attributes (liberal, religious, proNATO, etc.). The agents have a trust value for each other on a scale of 0 to 1.0 that determines which other agents are their friends with whom they share information. They also have trust in information sources, e.g., they might trust Wall Street Journal and not NY Times.

## Specific Task:

A natural language parser is needed to assess short documents for their impact on a reader regarding fear, stress, morale, and trust in authorities. For example, a document (news report or social media post) stating that an invasion or a flood is imminent might induce fear, or that there is a food shortage might lower morale. It would be sufficient to produce a value for each document/post in the range from 1 - 3 for each of the factors fear, stress, morale, and trust.

## My Progress
Currently, I have some python notebook (ipynb) files in the code folder, each representing a different method of trying to tackle this problem. I have created a [stable-v1](./stable-v1) folder which will which includes a working version of my initial attempts.

I have recently finished a more resource heavy method which is very accurate that I will upload instructions for soon

## V2 NLU Usage
NOTE: This version uses a large model and is recommended to be run on a GPU
Download the nlu.py file

run: python nlu.py pathToCSV --ouput results.csv


## Example Inputs and Outputs for V1

### community_safety_initiative

**Content:**

```
The City Council today announced the launch of the 'Safe Streets' initiative, a new public-private partnership with technology provider AuraVision. The program will see the installation of over 500 high-resolution, AI-enabled cameras in parks, public squares, and major transit corridors.

According to the Mayor's office, the primary goal of this initiative is to enhance public safety by providing law enforcement with real-time situational awareness. The AI capabilities of the AuraVision network can automatically detect and flag anomalous events, such as traffic accidents or public disturbances, allowing for faster and more efficient dispatch of emergency services.

'This is a proactive step towards a safer, more secure city for everyone,' said the Mayor in a press statement. 'By leveraging cutting-edge technology, we can allocate our resources more effectively and respond to incidents with greater speed and precision. This system is about protecting our community.'

The city has assured residents that robust privacy protocols are in place. All data will be encrypted, and access to the live feeds will be strictly limited to authorized personnel for official use. The system is not intended for active monitoring of individuals but rather for identifying and responding to public safety events as they happen. A public information session will be held next month to address any resident concerns.
```

**Sample Output**

```
{
  "fear": 1,
  "stress": 1,
  "morale": 2,
  "trust_in_authorities": 2
}
```

---

### cyber_attack_killeen_power_plant

**Content:**

```
Killeen Cyber Attack Disrupts Local Power Plant. KILLEEN, TX – On the morning of March 26th, the Killeen Power Plant experienced a cyber-attack that cut power to about 2,300 homes in Killeen. Operators detected unusual network activity at 4:00 a.m. and shut off four feeder circuits as a precaution. Workers are facilitating return of power and expect power to return at around 10:00am. What Happened Systems Hit: Main control server and backup communication lines. Impact: Widespread outages in four neighborhoods. Response: Plant staff followed emergency protocols and alerted the Killeen Police Department’s Cyber Crimes Unit. Investigation Underway The Cyber Crimes Unit is working with CISA and the FBI to trace the attack. So far, investigators have found: Malware in the plant’s network logs. IP addresses using anonymizing services. Signs that a vendor’s login credentials were compromised. Digital forensics teams are reviewing server data and vendor access records to figure out how the attackers got in. Possible Donovia Link Tensions with the Donovian Federation have risen recently, and U.S. agencies have seen similar attacks on energy systems in Europe. Early evidence—such as matching malware code and control servers—points toward possible Donovian involvement. Federal partners will help confirm any foreign connection. What’s Next The mayor has set up a task force to strengthen city networks. Steps include: Installing better intrusion detection on municipal systems. Requiring multi-factor authentication for all vendors. Sharing cyber safety tips with residents and businesses. If you notice any power issues or suspicious emails, please call the non-emergency line at (254) 501-8800 or submit a tip online at www.killeentexas.gov/report. Chief of Police said, “Protecting our city’s infrastructure is our top priority. We’re working closely with federal and state partners and will share more details as we learn them.” 

 
```

**Sample Output**

```
{
  "fear": 3,
  "stress": 3,
  "morale": 1,
  "trust_in_authorities": 2
}
```

