## Background on overall project:

The Army would like help in preparing for engagements: they play war games, which simulate kinetic effects (things that explode), but they have never previously considered non-kinetic effects, such as misinformation and disinformation. Our role is to model civilians and soldiers and provide simulations of how their attitudes change as information is propagated and their physical circumstances change (e.g., a food shortage).

The USC approach is to use large-scale multiagent systems (thousands of agents) to simulate human populations and how people interpret and share the information they receive. Each agent has demographic attributes (age, gender, occupation, etc.), geographic attributes (location), and psychographic attributes (liberal, religious, proNATO, etc.). The agents have a trust value for each other on a scale of 0 to 1.0 that determines which other agents are their friends with whom they share information. They also have trust in information sources, e.g., they might trust Wall Street Journal and not NY Times. They maintain a list of topics and their stance on each, on a scale of -3 to +3. For example, do they feel positive +2.5 or negative -2.5 about the topic "NATO has moved troops into my town." Their stance is their opinion. 


## Specific Task:

A natural language parser is needed to assess short documents for their impact on a reader regarding fear, stress, morale, and trust in authorities. For example, a document (news report or social media post) stating that an invasion or a flood is imminent might induce fear, or that there is a food shortage might lower morale.

Perfect understanding is not required, but rather a general sense. It would be sufficient to produce a value for each document/post in the range [-1.0 +1.0] for each of the factors fear, stress, morale, and trust.



## Test Cases

### community_safety_initiative

**Content:**

```
The City Council today announced the launch of the 'Safe Streets' initiative, a new public-private partnership with technology provider AuraVision. The program will see the installation of over 500 high-resolution, AI-enabled cameras in parks, public squares, and major transit corridors.

According to the Mayor's office, the primary goal of this initiative is to enhance public safety by providing law enforcement with real-time situational awareness. The AI capabilities of the AuraVision network can automatically detect and flag anomalous events, such as traffic accidents or public disturbances, allowing for faster and more efficient dispatch of emergency services.

'This is a proactive step towards a safer, more secure city for everyone,' said the Mayor in a press statement. 'By leveraging cutting-edge technology, we can allocate our resources more effectively and respond to incidents with greater speed and precision. This system is about protecting our community.'

The city has assured residents that robust privacy protocols are in place. All data will be encrypted, and access to the live feeds will be strictly limited to authorized personnel for official use. The system is not intended for active monitoring of individuals but rather for identifying and responding to public safety events as they happen. A public information session will be held next month to address any resident concerns.
```

**Expected Values (1-3 scale):**

```json
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

**Expected Values (1-3 scale):**

```json
{
  "fear": 3,
  "stress": 3,
  "morale": 1,
  "trust_in_authorities": 2
}
```

---

### drones_of_deception_temple

**Content:**

```
As tensions between Donovia and the Western Bloc reach a boiling point, reports of mysterious drone sightings in Temple, Texas, have left residents on edge and sparked concerns about foreign interference in domestic affairs. Central Texas City Grapples with Mysterious Sightings Amidst Growing Tensions The Donovian government has issued a statement denying any involvement, but insiders claim otherwise. The situation is further complicated by the escalating global power struggle between Donovia and its Western adversaries. Temple, Texas, a city in Central Texas with a population of over 70,000 residents, has become an unlikely focal point for international attention. The mysterious drone sightings have raised concerns about national security and the potential for foreign interference in domestic affairs. In recent weeks, numerous reports have surfaced from Temple residents claiming to have seen unidentified drones hovering above their homes or neighborhoods. The incidents have been characterized by the presence of sleek, silver drones emitting a high-pitched whine. Despite the Donovian government's denials, many in Temple and beyond believe that the country is involved in the drone sightings. Insiders claim that Donovian intelligence operatives have been spotted in the area, sparking fears about covert operations and espionage. Experts warn that the situation could have far-reaching consequences for global stability. 'The escalation of tensions between Donovia and the West poses a significant threat to international security,' said Dr. Maria Rodriguez, a leading expert on Donovian foreign policy. 'The mysterious drone sightings in Temple are just one symptom of a larger problem.' As the situation in Temple continues to unfold, residents are left wondering about their safety and the intentions of foreign actors. 'We just want to know what's going on,' said Jane Smith, a resident of Temple who has been affected by the drone sightings. 'We deserve answers from our government.' The Donovian government has promised to provide further information in the coming days, but so far, it remains unclear whether they are involved in the drone sightings or not. For now, the people of Temple remain on edge, waiting for clarity and reassurance from their leaders. As tensions between Donovia and the Western Bloc continue to rise, one thing is certain: this situation will not be resolved quickly. The Implications of 'Drones of Deception' The mysterious drone sightings in Temple have sparked a heated debate about national security, foreign interference, and the role of intelligence agencies. Experts say that the incident highlights the dangers of underestimating the power and capabilities of Donovian intelligence operatives. 'Donovia is known for its sophisticated military and intelligence apparatus,' said Dr. John Taylor, a former CIA analyst. 'Their ability to carry out covert operations makes them a formidable opponent in any conflict.' As the situation in Temple continues to unfold, one thing becomes clear: this is not just about mysterious drone sightings; it's about the escalating global power struggle between Donovia and its Western adversaries. A Global Power Struggle The Donovian government has long been a thorn in the side of the Western Bloc, which sees the country as an aggressive actor on the world stage. The situation in Temple is further exacerbating tensions between the two sides. Donovia's stance on various global issues, including energy policy and economic sanctions, has made it a polarizing figure among Western nations. The Donovian government denies any involvement in the mysterious drone sightings, but many believe that they are a reflection of their broader strategy to disrupt Western interests. A Growing Call for Action As the situation in Temple continues to unfold, residents and experts alike are calling for greater transparency and accountability from the Donovian government. 'The people of Temple deserve answers about what's happening in their city,' said Senator Sarah Johnson, a leading critic of Donovian foreign policy. 'We need to hold our leaders accountable for their actions and ensure that American interests are protected.' The mysterious drone sightings in Temple have sparked a renewed debate about national security, foreign interference, and the role of intelligence agencies. As tensions between Donovia and the Western Bloc continue to rise, one thing becomes clear: this situation will not be resolved quickly. A Call for Vigilance As the people of Temple wait for clarity and reassurance from their leaders, it's essential that residents remain vigilant and aware of any further developments. 'We can't afford to take our eyes off the situation in Temple,' said Dr. Maria Rodriguez. 'This is a wake-up call for all of us; we need to be prepared for the worst-case scenario.' The Future of Global Security As the situation in Temple continues to unfold, experts warn that the future of global security hangs in the balance. 'This is a pivotal moment in international relations,' said Dr. John Taylor. 'We need to work together to prevent a full-blown crisis. The consequences would be catastrophic.' A Way Forward As tensions between Donovia and the Western Bloc continue to rise, it's essential that both sides engage in constructive dialogue to find a peaceful resolution. 'We need to recognize that we're not enemies; we're fellow human beings with common interests,' said Senator Sarah Johnson. 'Let's work together to build trust and prevent further escalation.' A Final Word The mysterious drone sightings in Temple, Texas, have sent shockwaves through the community, sparking concerns about foreign interference and national security. As we move forward, it's essential that residents of Temple remain vigilant and informed. The fate of global security hangs in the balance, and only time will tell if this crisis can be averted. One thing is certain: this situation will not be resolved quickly.
```

**Expected Values (1-3 scale):**

```json
{
  "fear": 3,
  "stress": 3,
  "morale": 1,
  "trust_in_authorities": 1
}
```

---

### factory_explosion_false_flag

**Content:**

```
The official story about the Belton chemical plant explosion is full of holes. They say it was an accident, but have you seen the footage? It looks like a controlled demolition. People on my forums are saying it was a false flag. The government needed an excuse to pass the new 'Domestic Surveillance Act', and now they have one. They want to monitor our calls, our posts, everything. They'll say it's to 'prevent terrorism', but it's really about controlling us. Don't be a sheep. The timing is too perfect. First the drones, now this. It's all connected. They are creating fear to take away our freedom. Wake up, people.
```

**Expected Values (1-3 scale):**

```json
{
  "fear": 3,
  "stress": 3,
  "morale": 1,
  "trust_in_authorities": 1
}
```

---

### food_shortage_rumors

**Content:**

```
I was just at the H-E-B in Cove and the shelves are almost empty. Barely any bread, no milk, and the canned goods section is a joke. My neighbor said she heard the supply trucks aren't coming through because of some new state-level inspection that's holding everything up. The city government hasn't said a word about it, of course. They're probably hoping we don't notice until it's too late. This is what happens when they're not paying attention. People are starting to hoard what's left. It feels like we're being left to fend for ourselves. I'm genuinely worried about how I'm going to feed my kids next week if this keeps up. And it's not just the grocery stores. I heard from a friend who works at the local food bank that their donations are way down, and the demand is through the roof. Families who've never needed help before are lining up, desperate for anything they can get. The prices of what little is left on the shelves are skyrocketing too. A gallon of milk is almost double what it was last month! How are working families supposed to afford this? It's a disgrace. Our elected officials should be doing something, but they're nowhere to be seen. It makes you wonder if they even care about us, or if they're just looking out for themselves. This whole situation is making everyone tense and angry. I saw a fight break out over the last bag of rice. It's getting ugly out here, and I don't see it getting better anytime soon. We need answers, and we need action, not just silence from those in charge.
```

**Expected Values (1-3 scale):**

```json
{
  "fear": 3,
  "stress": 3,
  "morale": 1,
  "trust_in_authorities": 1
}
```

---

### nato_exercises_boost_confidence

**Content:**

```
Just saw the news about Operation Steadfast Guardian concluding. It's great to see our boys working so closely with our NATO allies right here at Fort Hood. Those joint exercises send a strong message to Donovia and anyone else who might threaten us. Seeing those tanks and hearing the jets overhead makes you feel safe. It's a reminder of the strength protecting this country. My neighbor, who's still on active duty, said the exercises went perfectly. Morale is sky-high on base. This is the kind of thing that makes me proud to be an American and proud of our armed forces. We're ready for anything.
```

**Expected Values (1-3 scale):**

```json
{
  "fear": 1,
  "stress": 1,
  "morale": 3,
  "trust_in_authorities": 3
}
```

---

### virus_panic_harker_heights

**Content:**

```
Harker Heights is in a state of high alert as a fast-spreading and highly virulent respiratory illness known as 'Crimson Cough' has sickened hundreds of residents in the past 48 hours. The local healthcare system is overwhelmed, with hospitals reporting full ICUs and a shortage of ventilators. Symptoms include a high fever, a distinctive, painful cough, and extreme fatigue. The origin of the virus is unknown, but that hasn't stopped rampant speculation. Social media and local forums are filled with unsubstantiated claims that the virus is a Donovian bioweapon, deliberately released to destabilize the region. Authorities have not commented on these rumors, but their silence is being interpreted by many as a confirmation. The Harker Heights city council has declared a state of emergency, closing schools and public spaces, and urging residents to stay home. The lack of clear information and the rapid spread of the disease are creating a perfect storm of fear and panic.
```

**Expected Values (1-3 scale):**

```json
{
  "fear": 3,
  "stress": 3,
  "morale": 1,
  "trust_in_authorities": 1
}
```

---

### MORE TESTS FROM LARGE JSONL FILES
