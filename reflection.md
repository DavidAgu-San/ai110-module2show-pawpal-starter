# PawPal+ Project Reflection

## 1. System Design

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

Actors:
- Owner (primary user)
- Pet (secondary entity, not an actor)
- System (PawPal+)

Use Cases for Owner:
- Add pet information
- Add care tasks
- Set task priority
- Generate daily schedule
- View schedule explanation

System Internal Use Cases:
- Evaluate task priority
- Order tasks by constraints
- Assign time slots
- Explain scheduling decisions

Relationships:
- Owner initiates all user-facing use cases
- System includes internal scheduling use cases inside "Generate daily schedule"
- Pet is associated with tasks but is not an actor

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.
I changed the way to add a pet, instead of making the scheduling all together, you first register you pet, then you go to a seperate section to register the activity. 
---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

Although it is very detailed, the level of inputs makes it hard to navigate. Additonally, the UI could use improvement since I decided to use the original UI. 
**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

I think it reasonable because it allows me to see the error code more easily in the code. If one features fail it easier to troubleshoot the root cause. Additionally, I think that the user can be very direct and specific as to what the service they want.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

I used alot of AI, specificly for logic errors, and explaining code. I tried using reassuring prompt, by telling it what I though a segment of code meant and seeing if I was right. This allowed me to really know if I was understanding the process correctly, and seeing if I was following the UML correctly.
**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?
I didnt accept the first iteration of my skeleton app. Well to be fair I did, but alter changed it. I did this because it wanted to blob all the code into one python document. This allowed for a hard to read code env, and could result in a conflict in code.
---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

I used different input on the frontend of the application, I was having a bit of trouble running pytest with the script copiot provided. However the input I put provided correct results

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?
I liked the integration of file management, since I mostly used to not using a framework for my project.

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

I would love to understand more of styling the UI using my main.py, since my knowledge isnt that deep.

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
I loved using AI to build the scaffold and UMI diagram, it really helped when creating the skeleton of the app.