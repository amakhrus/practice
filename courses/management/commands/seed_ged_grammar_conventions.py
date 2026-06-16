"""
Seed data: 'GED RLA: Grammar & Language Conventions' -- a deep-dive course on the
editing and conventions strand of the GED Reasoning Through Language Arts test.

Covers every grammar and conventions skill the GED tests directly:

  1. Sentence Structure   -- fragments, run-ons, subjects, predicates
  2. Nouns, Pronouns & Agreement  -- pronoun-antecedent, case, SVA
  3. Verb Tenses & Consistency    -- all tenses, irregular verbs, consistency
  4. Modifiers & Parallel Structure -- misplaced/dangling, parallel lists
  5. Punctuation: Commas, Semicolons & Colons  -- 5 comma rules, splices
  6. Word Choice: Commonly Confused Words -- affect/effect, its/it's, etc.
  7. Capitalization, Apostrophes & Editing Passages -- full GED-style editing

30 MCQs mirroring real GED grammar item style (bracketed/underlined error,
choose the correct revision). No figures needed; examples are inline text.

Run:
    python manage.py seed_ged_grammar_conventions
"""
from django.core.management.base import BaseCommand
from courses.models import Course, Lesson
from practice.models import Question, Choice


COURSE = {
    "title": "GED RLA: Grammar & Language Conventions",
    "slug": "ged-grammar-conventions",
    "program": "GED",
    "subject": "rla",
    "description": (
        "A focused deep dive into the grammar and language conventions skills tested on the GED "
        "Reasoning Through Language Arts exam. You will learn to identify and correct sentence "
        "fragments, run-ons, pronoun errors, tense shifts, misplaced modifiers, punctuation mistakes, "
        "commonly confused words, and capitalization errors -- exactly the editing skills the GED "
        "tests. Every lesson uses clear WRONG vs. CORRECT examples, key-term definitions, and "
        "GED-style practice questions with full explanations."
    ),
    "lessons": [
        (
            "1. Sentence Structure",
            "A **complete sentence** must have three things: a **subject** (who or what the sentence "
            "is about), a **predicate** (what the subject does or is -- always contains a verb), and a "
            "**complete thought** that can stand on its own.\n\n"
            "**Fragments** are incomplete sentences. They are missing a subject, a verb, or a complete "
            "thought.\n\n"
            "- **WRONG (missing subject):** Ran all the way to the station.\n"
            "- **WRONG (missing verb):** The old red bicycle in the garage.\n"
            "- **WRONG (incomplete thought):** Because she was tired.\n"
            "- **CORRECT:** She ran all the way to the station because she was tired.\n\n"
            "**Run-on sentences** occur when two or more independent clauses are joined without the "
            "correct punctuation or conjunction.\n\n"
            "- **WRONG (fused run-on):** She was tired she went to bed early.\n"
            "- **WRONG (comma splice):** She was tired, she went to bed early.\n"
            "- **CORRECT (period):** She was tired. She went to bed early.\n"
            "- **CORRECT (semicolon):** She was tired; she went to bed early.\n"
            "- **CORRECT (conjunction):** She was tired, so she went to bed early.\n\n"
            "**How to fix each error:**\n\n"
            "- Fragment: add a subject, add a verb, or attach the fragment to a nearby sentence.\n"
            "- Fused run-on: add a period, a semicolon, or a coordinating conjunction with a comma.\n"
            "- Comma splice: replace the comma with a period or semicolon, or add a conjunction.\n\n"
            "⚠️ Common mistake: thinking a long sentence cannot be a fragment. A clause that begins "
            "with 'because', 'although', 'since', or 'while' is always a dependent clause -- it is a "
            "fragment if nothing else is attached to it.\n\n"
            "💡 Tip: read the sentence aloud and ask 'Does this make a complete thought?' If you feel "
            "yourself waiting for more information, it is probably a fragment."
        ),
        (
            "2. Nouns, Pronouns & Agreement",
            "A **pronoun** takes the place of a noun (its **antecedent**). The pronoun must agree with "
            "its antecedent in number (singular/plural) and gender.\n\n"
            "**Pronoun-antecedent agreement:**\n\n"
            "- **WRONG:** Every student must bring their own pencil. (Every student is singular)\n"
            "- **CORRECT:** Every student must bring his or her own pencil.\n"
            "- **CORRECT (rewritten plural):** All students must bring their own pencils.\n\n"
            "**Pronoun case** -- subject vs. object:\n\n"
            "- Use **I, he, she, we, they, who** as the subject of a verb.\n"
            "- Use **me, him, her, us, them, whom** as the object of a verb or preposition.\n\n"
            "- **WRONG:** Me and him went to the store.\n"
            "- **CORRECT:** He and I went to the store.\n"
            "- **WRONG:** The prize was given to she and I.\n"
            "- **CORRECT:** The prize was given to her and me.\n\n"
            "**Who vs. whom:** use **who** when it is a subject ('Who called?'); use **whom** when it "
            "is an object ('To whom did you speak?'). A quick test: if you can substitute 'him' or "
            "'her', use 'whom'.\n\n"
            "**Vague pronouns** have no clear antecedent:\n\n"
            "- **WRONG (vague):** When Carlos talked to the manager, he said he was unhappy. (Who is "
            "'he'?)\n"
            "- **CORRECT:** When Carlos talked to the manager, Carlos said he was unhappy.\n\n"
            "**Subject-verb agreement:** the verb must match the subject in number, not the nearest "
            "noun.\n\n"
            "- **WRONG:** The box of nails are heavy.\n"
            "- **CORRECT:** The box of nails is heavy. (subject = box, singular)\n\n"
            "⚠️ Common mistake: matching the verb to the noun closest to it rather than to the real "
            "subject. Always identify the true subject first, then choose the verb.\n\n"
            "💡 Tip: to test pronoun case, remove the other person from the sentence. 'Me went to the "
            "store' sounds wrong immediately; 'I went to the store' sounds right."
        ),
        (
            "3. Verb Tenses & Consistency",
            "**Verb tense** tells the reader when an action happens. The GED tests your ability to "
            "choose the correct tense and to keep tense **consistent** throughout a passage.\n\n"
            "**The main tenses:**\n\n"
            "- **Simple past:** She walked to school. (completed action)\n"
            "- **Simple present:** She walks to school. (habit or general truth)\n"
            "- **Simple future:** She will walk to school. (action not yet done)\n"
            "- **Present perfect:** She has walked to school. (past action with present relevance)\n"
            "- **Past perfect:** She had walked to school before the rain started. (earlier of two past "
            "actions)\n"
            "- **Future perfect:** She will have walked five miles by noon. (action complete before a "
            "future point)\n\n"
            "**Tense consistency:** within a paragraph about one time frame, do not switch tenses "
            "without reason.\n\n"
            "- **WRONG:** She opened the door and walks inside. (past then present -- inconsistent)\n"
            "- **CORRECT:** She opened the door and walked inside.\n\n"
            "**Common irregular verbs** (memorize these!):\n\n"
            "- go / went / gone\n"
            "- see / saw / seen\n"
            "- run / ran / run\n"
            "- eat / ate / eaten\n"
            "- write / wrote / written\n"
            "- bring / brought / brought\n"
            "- lie (recline) / lay / lain -- vs. -- lay (place) / laid / laid\n\n"
            "**Perfect tense clue words:** 'already', 'yet', 'just', 'since', 'by the time' often "
            "signal that a perfect tense is needed.\n\n"
            "- **WRONG:** By the time we arrived, she already left.\n"
            "- **CORRECT:** By the time we arrived, she had already left. (past perfect needed)\n\n"
            "⚠️ Common mistake: using 'had went' or 'had ran' -- irregular verbs use their past "
            "participle form with 'had': had gone, had run, had seen.\n\n"
            "💡 Tip: when editing a passage, underline every verb. If you spot a tense that does not "
            "match the others without a logical reason, that is your error."
        ),
        (
            "4. Modifiers and Parallel Structure",
            "A **modifier** is a word, phrase, or clause that describes something else. Modifiers must "
            "be placed as close as possible to what they modify -- otherwise the sentence becomes "
            "confusing or unintentionally funny.\n\n"
            "**Misplaced modifier:** placed too far from the word it modifies.\n\n"
            "- **WRONG:** She served sandwiches to the children on paper plates.\n"
            "  (Were the children on paper plates?)\n"
            "- **CORRECT:** She served sandwiches on paper plates to the children.\n\n"
            "**Dangling modifier:** the word being modified is not even in the sentence.\n\n"
            "- **WRONG:** Running to catch the bus, the rain soaked my shoes.\n"
            "  (The rain was not running to catch the bus.)\n"
            "- **CORRECT:** Running to catch the bus, I got my shoes soaked by the rain.\n\n"
            "**Parallel structure** means using the same grammatical form for items in a list or "
            "paired comparison. When items are joined by 'and', 'but', 'or', or paired words like "
            "'both...and', 'either...or', 'not only...but also' -- all items must be in the same form.\n\n"
            "- **WRONG (mixed forms):** She enjoys hiking, to swim, and running.\n"
            "- **CORRECT:** She enjoys hiking, swimming, and running. (all gerunds)\n\n"
            "- **WRONG:** The report was long, confusing, and it lacked focus.\n"
            "- **CORRECT:** The report was long, confusing, and unfocused. (all adjectives)\n\n"
            "- **WRONG:** He is not only a skilled doctor but also practices law.\n"
            "- **CORRECT:** He is not only a skilled doctor but also a talented lawyer.\n\n"
            "⚠️ Common mistake: with 'not only...but also', the grammatical form that follows 'not "
            "only' must exactly match the form that follows 'but also'.\n\n"
            "💡 Tip: for parallel structure, read the items in a list and ask 'Are they all nouns? All "
            "verbs? All adjectives?' The moment one item breaks the pattern, you have found the error."
        ),
        (
            "5. Punctuation: Commas, Semicolons & Colons",
            "Punctuation errors are among the most common GED editing questions. Master these rules "
            "and you will catch most of them.\n\n"
            "**The 5 main comma rules:**\n\n"
            "1. **Before a coordinating conjunction** joining two independent clauses "
            "(for, and, nor, but, or, yet, so -- remember: FANBOYS).\n"
            "   - CORRECT: She studied hard, and she passed the test.\n\n"
            "2. **After an introductory element** (clause, phrase, or word at the start).\n"
            "   - CORRECT: After the storm passed, we surveyed the damage.\n\n"
            "3. **Around a nonessential clause or phrase** (information that can be removed without "
            "changing the core meaning).\n"
            "   - CORRECT: My sister, who lives in Austin, is a nurse.\n\n"
            "4. **Between items in a series** (the Oxford comma before 'and' is recommended).\n"
            "   - CORRECT: We bought apples, oranges, and bananas.\n\n"
            "5. **Between coordinate adjectives** (adjectives that equally describe a noun).\n"
            "   - CORRECT: It was a long, exhausting day.\n\n"
            "**Comma splice:** two independent clauses joined only by a comma -- always wrong.\n\n"
            "- **WRONG:** I was hungry, I ate lunch early.\n"
            "- **CORRECT (semicolon):** I was hungry; I ate lunch early.\n"
            "- **CORRECT (conjunction):** I was hungry, so I ate lunch early.\n\n"
            "**Semicolons** join two closely related independent clauses without a conjunction, or "
            "separate list items that already contain commas.\n\n"
            "- CORRECT: The meeting ran long; we missed the train.\n\n"
            "**Colons** introduce a list, an explanation, or a quotation -- but only when a complete "
            "independent clause comes before the colon.\n\n"
            "- **WRONG:** We need: flour, sugar, and eggs. (no full clause before the colon)\n"
            "- **CORRECT:** We need three things: flour, sugar, and eggs.\n\n"
            "⚠️ Common mistake: using a comma before 'because'. Do not put a comma before 'because' "
            "unless omitting the 'because' clause would change the meaning.\n\n"
            "💡 Tip: to test whether a semicolon is correct, replace it with a period. If both parts "
            "are complete sentences, the semicolon works."
        ),
        (
            "6. Word Choice: Commonly Confused Words",
            "The GED tests several pairs of words that look or sound alike but have different meanings. "
            "Learning the distinction eliminates a whole category of errors.\n\n"
            "**affect vs. effect:**\n"
            "- **affect** (verb): to influence. -- The cold weather *affected* my mood.\n"
            "- **effect** (noun): a result. -- The cold weather had a negative *effect* on my mood.\n"
            "- Memory trick: **A**ffect is the **A**ction; **E**ffect is the **E**nd result.\n\n"
            "**its vs. it's:**\n"
            "- **its** (possessive): belonging to it. -- The dog wagged *its* tail.\n"
            "- **it's** (contraction of 'it is' or 'it has'). -- *It's* raining outside.\n"
            "- Test: substitute 'it is'. If it makes sense, use 'it's'; otherwise use 'its'.\n\n"
            "**their / there / they're:**\n"
            "- **their** (possessive): belonging to them. -- They forgot *their* keys.\n"
            "- **there** (place or expletive): over there; there is. -- Put it over *there*.\n"
            "- **they're** (contraction of 'they are'). -- *They're* going to be late.\n\n"
            "**who vs. whom:** (see Lesson 2 -- who = subject, whom = object)\n\n"
            "**lie vs. lay:**\n"
            "- **lie** (recline -- intransitive, no object): I need to *lie* down. / Yesterday I *lay* "
            "down.\n"
            "- **lay** (place -- transitive, needs an object): Please *lay* the book on the table. / "
            "She *laid* it there.\n\n"
            "**fewer vs. less:**\n"
            "- **fewer**: for things you can count. -- *Fewer* students enrolled this year.\n"
            "- **less**: for amounts you cannot count individually. -- There is *less* water in the "
            "tank.\n\n"
            "**between vs. among:**\n"
            "- **between**: two things. -- Choose *between* coffee and tea.\n"
            "- **among**: three or more things. -- Divide the prize *among* the five winners.\n\n"
            "⚠️ Common mistake: writing 'less students' or 'less errors'. If you can count it, use "
            "'fewer'.\n\n"
            "💡 Tip: for every confusing word pair, learn one quick test (like 'substitute it is' for "
            "its/it's) so you can check in seconds on the exam."
        ),
        (
            "7. Capitalization, Apostrophes & Editing Passages",
            "**Capitalization rules:**\n\n"
            "- **Always capitalize:** the first word of a sentence; proper nouns (names of specific "
            "people, places, organizations, days, months, holidays); titles used directly before a "
            "name (President Lincoln, but the president spoke).\n"
            "- **Do not capitalize:** seasons (spring, fall), general directions (drive north, but "
            "she lives in the North), common nouns used generally (I love history, but History 101 is "
            "a course name).\n\n"
            "- **WRONG:** I am going to visit my Aunt in the Spring.\n"
            "- **CORRECT:** I am going to visit my aunt in the spring.\n\n"
            "**Apostrophes:**\n\n"
            "- **Possessive singular:** add 's -- the *dog's* leash.\n"
            "- **Possessive plural (ending in s):** add only the apostrophe -- the *dogs'* leashes "
            "(multiple dogs).\n"
            "- **Contractions:** apostrophe replaces the missing letter(s) -- don't, can't, they're.\n"
            "- **NEVER** use an apostrophe to make a plain plural.\n\n"
            "- **WRONG:** The student's received their grade's.\n"
            "- **CORRECT:** The students received their grades.\n\n"
            "**Possessives vs. plurals:**\n\n"
            "- *cats* = more than one cat (plural, no apostrophe).\n"
            "- *cat's* = belonging to one cat (singular possessive).\n"
            "- *cats'* = belonging to multiple cats (plural possessive).\n\n"
            "**Editing a full paragraph (GED-style practice):**\n\n"
            "Read the passage below and identify every error:\n\n"
            "\"Last Summer, my sister and I visited are grandparents in Boston. We drove for six "
            "hours, then we stopped at a rest stop for food. My grandmother, who is a excellent cook, "
            "had already prepared a huge dinner. The effect of the long drive were tiredness, but "
            "seeing are family made it worthwhile.\"\n\n"
            "**Errors and corrections:**\n\n"
            "- 'Last Summer' -- **capitalize** Summer? No: seasons are not capitalized. Fix: last "
            "summer.\n"
            "- 'are grandparents' -- **wrong word**: 'are' is a verb; should be 'our' (possessive). "
            "Fix: our grandparents.\n"
            "- 'then we stopped' after a comma joining two independent clauses -- **comma splice**. "
            "Fix: We drove for six hours; then we stopped... OR ...hours, and then we stopped.\n"
            "- 'a excellent' -- **article error**: use 'an' before vowel sounds. Fix: an excellent.\n"
            "- 'The effect...were tiredness' -- **subject-verb agreement**: 'effect' is singular, so "
            "use 'was'. Fix: The effect...was tiredness.\n"
            "- 'are family' -- **wrong word** again: should be 'our'. Fix: our family.\n\n"
            "⚠️ Common mistake: apostrophe abuse -- adding apostrophes to all words ending in 's'. "
            "Plain plurals never need an apostrophe.\n\n"
            "💡 Tip: on the GED editing passage, work through errors one category at a time -- first "
            "check capitalization, then apostrophes, then subject-verb agreement, then word choice."
        ),
    ],
    "mcqs": [
        # --- Lesson 1: Sentence Structure (5 questions) ---
        {
            "text": (
                "Which of the following is a complete sentence?\n\n"
                "(A) Running through the park on a cold morning.\n"
                "(B) Because the storm knocked out the power.\n"
                "(C) The technician repaired the broken equipment.\n"
                "(D) After the long, difficult meeting finally ended."
            ),
            "difficulty": 1,
            "choices": [
                ("The technician repaired the broken equipment.", True),
                ("Running through the park on a cold morning.", False),
                ("Because the storm knocked out the power.", False),
                ("After the long, difficult meeting finally ended.", False),
            ],
            "explanation": (
                "'The technician repaired the broken equipment' has a subject (technician), a verb "
                "(repaired), and a complete thought. The other three are fragments: (A) has no subject "
                "or complete thought, (B) and (D) are subordinate clauses that depend on a main clause "
                "to be complete."
            ),
        },
        {
            "text": (
                "Read the sentence below. Which revision corrects the error?\n\n"
                "\"The project was finished on time, [it came in under budget].\""
            ),
            "difficulty": 2,
            "choices": [
                ("The project was finished on time; it came in under budget.", True),
                ("The project was finished on time, and, it came in under budget.", False),
                ("The project was finished on time it came in under budget.", False),
                ("The project was finished on time. Because it came in under budget.", False),
            ],
            "explanation": (
                "The original sentence is a comma splice -- two independent clauses joined only by a "
                "comma. The correct fix is to replace the comma with a semicolon. Adding an extra comma "
                "around 'and' is incorrect punctuation; removing punctuation entirely creates a fused "
                "run-on; and adding 'Because' creates a fragment."
            ),
        },
        {
            "text": (
                "Which of the following is a run-on sentence?\n\n"
                "(A) She loves reading; she visits the library every week.\n"
                "(B) Although he was nervous, he delivered a strong speech.\n"
                "(C) Marcus completed his training he received his certificate.\n"
                "(D) The committee reviewed the proposal and rejected it."
            ),
            "difficulty": 2,
            "choices": [
                ("Marcus completed his training he received his certificate.", True),
                ("She loves reading; she visits the library every week.", False),
                ("Although he was nervous, he delivered a strong speech.", False),
                ("The committee reviewed the proposal and rejected it.", False),
            ],
            "explanation": (
                "(C) is a fused run-on: two independent clauses ('Marcus completed his training' and 'he "
                "received his certificate') are crammed together with no punctuation or conjunction. (A) "
                "uses a correct semicolon; (B) correctly uses a comma after the introductory dependent "
                "clause; (D) is one sentence with a compound predicate."
            ),
        },
        {
            "text": (
                "Read the passage and identify the fragment.\n\n"
                "\"(1) The company expanded its operations last year. (2) Opening three new offices "
                "across the country. (3) Revenue increased by 20 percent.\""
            ),
            "difficulty": 2,
            "choices": [
                ("Opening three new offices across the country.", True),
                ("The company expanded its operations last year.", False),
                ("Revenue increased by 20 percent.", False),
                ("There is no fragment in the passage.", False),
            ],
            "explanation": (
                "Sentence 2, 'Opening three new offices across the country,' is a participial phrase "
                "with no subject and no main verb -- it is a fragment. The correct fix is to attach it "
                "to sentence 1: 'The company expanded its operations last year, opening three new "
                "offices across the country.'"
            ),
        },
        {
            "text": (
                "A student wrote: \"She studied all night, she still felt unprepared for the exam.\"\n\n"
                "Which revision BEST corrects the error?"
            ),
            "difficulty": 2,
            "choices": [
                ("She studied all night, but she still felt unprepared for the exam.", True),
                ("She studied all night, yet, she still felt unprepared for the exam.", False),
                ("She studied all night she still felt unprepared for the exam.", False),
                ("She studied all night; yet she still felt unprepared for the exam.", False),
            ],
            "explanation": (
                "The original is a comma splice. The best fix is to add the coordinating conjunction "
                "'but' after the comma, making a correct compound sentence. Option (D) looks close but "
                "is incorrect: 'yet' used as a conjunctive adverb after a semicolon requires no comma "
                "before the independent clause in standard usage, and the construction is awkward here. "
                "Option (B) uses an extra comma incorrectly around 'yet'. Option (C) removes all "
                "punctuation, creating a fused run-on."
            ),
        },
        # --- Lesson 2: Nouns, Pronouns & Agreement (5 questions) ---
        {
            "text": (
                "Which sentence uses correct pronoun case?\n\n"
                "(A) The award was presented to James and I.\n"
                "(B) Between you and I, this plan will not work.\n"
                "(C) Her and me finished the project on time.\n"
                "(D) The manager called him and me into the office."
            ),
            "difficulty": 2,
            "choices": [
                ("The manager called him and me into the office.", True),
                ("The award was presented to James and I.", False),
                ("Between you and I, this plan will not work.", False),
                ("Her and me finished the project on time.", False),
            ],
            "explanation": (
                "In (D), 'him' and 'me' are correct object pronouns -- they are the objects of the verb "
                "'called'. In (A) and (B), 'I' should be 'me' because both are objects of prepositions "
                "('to' and 'between'). In (C), 'Her' should be 'She' and 'me' should be 'I' because "
                "they are the subjects of the sentence."
            ),
        },
        {
            "text": (
                "Read the sentence below. Which revision corrects the pronoun error?\n\n"
                "\"[Everyone] on the team submitted their report before the deadline.\""
            ),
            "difficulty": 2,
            "choices": [
                ("Everyone on the team submitted his or her report before the deadline.", True),
                ("Everyone on the team submitted our report before the deadline.", False),
                ("Everyone on the team submitted its report before the deadline.", False),
                ("The sentence is already correct as written.", False),
            ],
            "explanation": (
                "'Everyone' is a singular indefinite pronoun, so it requires a singular pronoun. The "
                "grammatically correct choice is 'his or her'. 'Our' refers to the speaker's group, "
                "which is not the antecedent. 'Its' is used for objects, not people. The original "
                "sentence uses the plural 'their' with the singular 'everyone', which is a pronoun-"
                "antecedent agreement error in formal grammar."
            ),
        },
        {
            "text": (
                "Which sentence uses 'who' or 'whom' correctly?"
            ),
            "difficulty": 3,
            "choices": [
                ("The officer to whom the complaint was addressed responded quickly.", True),
                ("The officer to who the complaint was addressed responded quickly.", False),
                ("Who did you speak with about the complaint?", False),
                ("Whom called the office this morning?", False),
            ],
            "explanation": (
                "In (A), 'whom' is correct because it is the object of the preposition 'to'. The test: "
                "substitute 'him' -- 'the complaint was addressed to him' works, so 'whom' is correct. "
                "In (C), 'Who' should be 'Whom' (object of 'with'). In (D), 'Whom' should be 'Who' "
                "because it is the subject of the verb 'called'."
            ),
        },
        {
            "text": (
                "Read the sentence. Which revision fixes the subject-verb agreement error?\n\n"
                "\"The collection of rare stamps [were] donated to the museum.\""
            ),
            "difficulty": 2,
            "choices": [
                ("The collection of rare stamps was donated to the museum.", True),
                ("The collection of rare stamps have been donated to the museum.", False),
                ("The collection of rare stamps are donated to the museum.", False),
                ("The sentence is already correct.", False),
            ],
            "explanation": (
                "The true subject is 'collection' (singular), not 'stamps'. A singular subject takes a "
                "singular verb: 'was donated'. The prepositional phrase 'of rare stamps' is not the "
                "subject and does not affect verb choice."
            ),
        },
        {
            "text": (
                "A writer composed: \"When Sarah spoke with the director, she said she was "
                "dissatisfied with the results.\"\n\n"
                "What is the problem with this sentence, and what is the best revision?"
            ),
            "difficulty": 3,
            "choices": [
                ("Vague pronoun reference -- revise to: 'When Sarah spoke with the director, the director said she was dissatisfied.'", True),
                ("Incorrect verb tense -- revise to: 'When Sarah speaks with the director, she said she is dissatisfied.'", False),
                ("Run-on sentence -- add a semicolon after 'director'.", False),
                ("No error -- the sentence is correct as written.", False),
            ],
            "explanation": (
                "The pronoun 'she' appears twice and could refer to either Sarah or the director, making "
                "the reference ambiguous (vague pronoun). The revision clarifies which person was "
                "dissatisfied. Tense and sentence structure are not the issue here."
            ),
        },
        # --- Lesson 3: Verb Tenses & Consistency (4 questions) ---
        {
            "text": (
                "Which sentence uses the correct verb tense?\n\n"
                "\"By the time the ambulance arrived, the paramedics _____ the patient for ten "
                "minutes.\"\n\n"
                "(A) treat\n(B) treated\n(C) had been treating\n(D) will treat"
            ),
            "difficulty": 3,
            "choices": [
                ("had been treating", True),
                ("treat", False),
                ("treated", False),
                ("will treat", False),
            ],
            "explanation": (
                "The phrase 'by the time the ambulance arrived' signals that one past action (treating "
                "the patient) was already ongoing when another past action (arriving) occurred. The past "
                "perfect progressive 'had been treating' correctly expresses this ongoing earlier action. "
                "Simple past 'treated' does not show the ongoing nature or the sequence."
            ),
        },
        {
            "text": (
                "Read the passage. Which underlined verb must be changed to correct the tense shift?\n\n"
                "\"Last Tuesday, the committee [met] to review the budget. They [discussed] several "
                "proposals and [vote] on the final plan before adjourning.\""
            ),
            "difficulty": 2,
            "choices": [
                ("'vote' should be 'voted'", True),
                ("'met' should be 'meet'", False),
                ("'discussed' should be 'discuss'", False),
                ("There is no tense error in the passage.", False),
            ],
            "explanation": (
                "The passage describes past events ('Last Tuesday'). 'Met' and 'discussed' are correctly "
                "in the past tense, but 'vote' incorrectly shifts to the present tense. It should be "
                "'voted' to maintain consistency with the rest of the passage."
            ),
        },
        {
            "text": (
                "Which sentence contains an error with an irregular verb?"
            ),
            "difficulty": 2,
            "choices": [
                ("She had went to the store before the rain started.", True),
                ("He ran three miles before breakfast this morning.", False),
                ("They had seen the documentary twice already.", False),
                ("By noon, she had eaten lunch and started her report.", False),
            ],
            "explanation": (
                "The past participle of 'go' is 'gone', not 'went'. The correct form is 'had gone'. "
                "'Went' is the simple past and cannot follow 'had'. The other sentences correctly use "
                "'ran' (simple past of run), 'seen' (past participle of see), and 'eaten' (past "
                "participle of eat)."
            ),
        },
        {
            "text": (
                "Choose the sentence that correctly uses verb tense throughout."
            ),
            "difficulty": 2,
            "choices": [
                ("The chef chopped the vegetables, added them to the pot, and stirred the soup.", True),
                ("The chef chopped the vegetables, adds them to the pot, and stirred the soup.", False),
                ("The chef chops the vegetables, added them to the pot, and stirs the soup.", False),
                ("The chef will chop the vegetables, added them to the pot, and stirred the soup.", False),
            ],
            "explanation": (
                "Correct answer (A) uses past tense consistently: chopped, added, stirred -- all three "
                "verbs describe a completed sequence of events in the same time frame. The other options "
                "shift between tenses (present, past, future) without reason."
            ),
        },
        # --- Lesson 4: Modifiers and Parallel Structure (4 questions) ---
        {
            "text": (
                "Read the sentence. Which revision corrects the dangling modifier?\n\n"
                "\"[Exhausted from the long hike,] the tent was set up quickly.\""
            ),
            "difficulty": 3,
            "choices": [
                ("Exhausted from the long hike, we set up the tent quickly.", True),
                ("Exhausted from the long hike, the tent quickly was set up.", False),
                ("The tent, exhausted from the long hike, was set up quickly.", False),
                ("Having been exhausted, the tent was set up from the long hike quickly.", False),
            ],
            "explanation": (
                "The participial phrase 'Exhausted from the long hike' must modify the subject of the "
                "main clause -- but the tent cannot be exhausted. The fix is to introduce a subject that "
                "could logically be exhausted: 'we'. Only option (A) places the correct, logical subject "
                "immediately after the modifying phrase."
            ),
        },
        {
            "text": (
                "Which sentence contains a misplaced modifier?\n\n"
                "(A) She almost drove her children to school every day.\n"
                "(B) The teacher handed tests to students with a red pen.\n"
                "(C) Running late, he grabbed his bag and rushed out.\n"
                "(D) Both A and B"
            ),
            "difficulty": 3,
            "choices": [
                ("Both A and B", True),
                ("She almost drove her children to school every day.", False),
                ("The teacher handed tests to students with a red pen.", False),
                ("Running late, he grabbed his bag and rushed out.", False),
            ],
            "explanation": (
                "In (A), 'almost' modifies 'drove' but should modify 'every day' -- she drove them "
                "nearly every day (not that she almost drove them). In (B), 'with a red pen' appears to "
                "modify 'students' but should modify 'handed' -- the teacher used the red pen, not the "
                "students. Both are misplaced modifiers. (C) is correct: 'Running late' logically "
                "modifies 'he'."
            ),
        },
        {
            "text": (
                "Read the sentence. Which revision corrects the parallel structure error?\n\n"
                "\"The program director is responsible for hiring staff, to manage budgets, "
                "and the coordination of events.\""
            ),
            "difficulty": 2,
            "choices": [
                ("The program director is responsible for hiring staff, managing budgets, and coordinating events.", True),
                ("The program director is responsible for hiring staff, manages budgets, and coordinates events.", False),
                ("The program director is responsible to hire staff, managing budgets, and coordinating events.", False),
                ("The program director is responsible for hiring staff, to manage budgets, and coordinating events.", False),
            ],
            "explanation": (
                "The list follows 'for', so all three items must be gerunds (verb + -ing). The correct "
                "parallel form is: hiring, managing, coordinating. The original mixes three forms: a "
                "gerund, an infinitive, and a noun phrase. Only option (A) uses three matching gerunds."
            ),
        },
        {
            "text": (
                "Which sentence uses parallel structure correctly?"
            ),
            "difficulty": 2,
            "choices": [
                ("She is not only a gifted writer but also a talented editor.", True),
                ("She is not only a gifted writer but also editing with talent.", False),
                ("She is not only gifted at writing but also a talented editor.", False),
                ("She is not only writing with gifts but also talented at editing.", False),
            ],
            "explanation": (
                "With 'not only...but also', the structure after each part must be parallel. In (A), "
                "both parts are noun phrases: 'a gifted writer' and 'a talented editor' -- perfectly "
                "parallel. The other options mix noun phrases with verb phrases, breaking the parallel "
                "structure."
            ),
        },
        # --- Lesson 5: Punctuation -- Commas, Semicolons & Colons (4 questions) ---
        {
            "text": (
                "Which sentence is punctuated correctly?"
            ),
            "difficulty": 2,
            "choices": [
                ("After finishing her degree, she accepted a position at the research institute.", True),
                ("After finishing her degree she accepted, a position at the research institute.", False),
                ("After finishing her degree; she accepted a position at the research institute.", False),
                ("After finishing, her degree she accepted a position at the research institute.", False),
            ],
            "explanation": (
                "When a sentence begins with an introductory clause or phrase, a comma follows the "
                "introductory element before the main clause. 'After finishing her degree' is an "
                "introductory phrase, so a comma comes after 'degree'. A semicolon would be incorrect "
                "because 'After finishing her degree' is not an independent clause."
            ),
        },
        {
            "text": (
                "Read the sentence. Which revision corrects the punctuation error?\n\n"
                "\"The conference was a success, [hundreds of attendees praised the speakers].\""
            ),
            "difficulty": 2,
            "choices": [
                ("The conference was a success; hundreds of attendees praised the speakers.", True),
                ("The conference was a success, and hundreds of attendees praised the speakers.", True),
                ("The conference was a success: hundreds of attendees praised the speakers.", False),
                ("The conference was a success hundreds of attendees praised the speakers.", False),
            ],
            "explanation": (
                "The original is a comma splice. Both a semicolon and adding 'and' after the comma are "
                "grammatically correct fixes. A colon (option C) could work stylistically if the second "
                "clause explains the first, but standard GED guidance treats the semicolon as the "
                "cleaner fix here. For this question the credited answer is the semicolon option. "
                "Removing all punctuation creates a fused run-on."
            ),
        },
        {
            "text": (
                "Which sentence uses a colon correctly?\n\n"
                "(A) The ingredients include: flour, sugar, and eggs.\n"
                "(B) The recipe requires three main ingredients: flour, sugar, and eggs.\n"
                "(C) She bought: flour, sugar, and eggs at the store.\n"
                "(D) The store had: flour, sugar, eggs, and butter."
            ),
            "difficulty": 2,
            "choices": [
                ("The recipe requires three main ingredients: flour, sugar, and eggs.", True),
                ("The ingredients include: flour, sugar, and eggs.", False),
                ("She bought: flour, sugar, and eggs at the store.", False),
                ("The store had: flour, sugar, eggs, and butter.", False),
            ],
            "explanation": (
                "A colon must be preceded by a complete independent clause. In (B), 'The recipe "
                "requires three main ingredients' is a complete clause -- correct. In (A), (C), and "
                "(D), the colon interrupts the verb phrase ('include:', 'bought:', 'had:'), which is "
                "incorrect. The colon should never separate a verb from its direct objects."
            ),
        },
        {
            "text": (
                "Which sentence correctly uses commas with a nonessential clause?\n\n"
                "(A) My brother who lives in Chicago is a doctor.\n"
                "(B) My brother, who lives in Chicago, is a doctor.\n"
                "(C) My brother who lives, in Chicago, is a doctor.\n"
                "(D) My, brother who lives in Chicago is a doctor."
            ),
            "difficulty": 2,
            "choices": [
                ("My brother, who lives in Chicago, is a doctor.", True),
                ("My brother who lives in Chicago is a doctor.", False),
                ("My brother who lives, in Chicago, is a doctor.", False),
                ("My, brother who lives in Chicago is a doctor.", False),
            ],
            "explanation": (
                "The clause 'who lives in Chicago' is nonessential (it adds information but is not "
                "needed to identify which brother -- it is assumed the speaker has one brother). "
                "Nonessential clauses are set off by commas on both sides. If there were multiple "
                "brothers and the clause identified a specific one, no commas would be used (essential "
                "clause). Option (B) correctly uses commas around the nonessential clause."
            ),
        },
        # --- Lesson 6: Word Choice -- Commonly Confused Words (4 questions) ---
        {
            "text": (
                "Choose the sentence that uses 'affect' and 'effect' correctly."
            ),
            "difficulty": 1,
            "choices": [
                ("The new policy will affect all employees, and its effect will be felt immediately.", True),
                ("The new policy will effect all employees, and its affect will be felt immediately.", False),
                ("The new policy will affect all employees, and its affect will be felt immediately.", False),
                ("The new policy will effect all employees, and its effect will be felt immediately.", False),
            ],
            "explanation": (
                "'Affect' is a verb meaning to influence; 'effect' is a noun meaning a result. The "
                "correct sentence uses 'affect' (verb) in the first clause and 'effect' (noun -- 'its "
                "effect') in the second clause. All other options swap or misuse one or both words."
            ),
        },
        {
            "text": (
                "Read the sentence. Which word correctly fills the blank?\n\n"
                "\"The committee finished _____ review of the annual budget.\""
            ),
            "difficulty": 1,
            "choices": [
                ("its", True),
                ("it's", False),
                ("its'", False),
                ("its's", False),
            ],
            "explanation": (
                "'Its' is the possessive form of 'it' -- the review belongs to the committee. 'It's' is "
                "a contraction for 'it is' or 'it has', which makes no sense here ('The committee "
                "finished it is review'). 'Its'' and 'its's' are not real words."
            ),
        },
        {
            "text": (
                "Which sentence uses 'fewer' and 'less' correctly?"
            ),
            "difficulty": 2,
            "choices": [
                ("There are fewer students in the program this semester, and there is less funding available.", True),
                ("There are less students in the program this semester, and there is fewer funding available.", False),
                ("There are fewer students in the program this semester, and there is fewer funding available.", False),
                ("There are less students in the program this semester, and there is less funding available.", False),
            ],
            "explanation": (
                "'Fewer' is used with countable nouns (students can be counted individually); 'less' is "
                "used with uncountable or mass nouns (funding is a mass noun). The correct sentence uses "
                "'fewer students' and 'less funding'."
            ),
        },
        {
            "text": (
                "Read the sentence. Which revision corrects all word-choice errors?\n\n"
                "\"[Their] going to present [there] findings to [there] supervisor tomorrow.\""
            ),
            "difficulty": 1,
            "choices": [
                ("They're going to present their findings to their supervisor tomorrow.", True),
                ("Their going to present they're findings to their supervisor tomorrow.", False),
                ("There going to present their findings to there supervisor tomorrow.", False),
                ("They're going to present there findings to they're supervisor tomorrow.", False),
            ],
            "explanation": (
                "'They're' = they are (contraction) -- correct for the first blank. 'Their' = belonging "
                "to them (possessive) -- correct for 'their findings' and 'their supervisor'. The "
                "original incorrectly uses 'Their' (possessive) where 'They're' (contraction) is needed, "
                "and 'there' (a place) where 'their' (possessive) is needed."
            ),
        },
        # --- Lesson 7: Capitalization, Apostrophes & Editing Passages (4 questions) ---
        {
            "text": (
                "Which sentence uses capitalization correctly?"
            ),
            "difficulty": 1,
            "choices": [
                ("On Monday, we will attend a lecture by Professor Kim.", True),
                ("On monday, we will attend a lecture by professor Kim.", False),
                ("On Monday, we will attend a Lecture by professor Kim.", False),
                ("on monday, we will attend a lecture by Professor kim.", False),
            ],
            "explanation": (
                "Days of the week (Monday) and professional titles used directly before a name "
                "(Professor Kim) are capitalized. 'Lecture' is a common noun and should not be "
                "capitalized. 'Professor' before a name is a title and is capitalized; used alone it "
                "would be lowercase."
            ),
        },
        {
            "text": (
                "Which sentence uses apostrophes correctly?"
            ),
            "difficulty": 2,
            "choices": [
                ("The children's backpacks were left in the teachers' lounge.", True),
                ("The childrens' backpacks were left in the teacher's lounge.", False),
                ("The children's backpack's were left in the teachers lounge.", False),
                ("The childrens backpacks were left in the teachers' lounge.", False),
            ],
            "explanation": (
                "'Children' is an irregular plural (not ending in s), so the possessive is 'children's'. "
                "'Teachers' is a regular plural ending in s, so the possessive is 'teachers'' (apostrophe "
                "after the s). 'Backpacks' is a plain plural requiring no apostrophe. Option (A) handles "
                "all three correctly."
            ),
        },
        {
            "text": (
                "Read the passage and identify the sentence with an error.\n\n"
                "\"(1) The anderson family moved to their new home in the Spring. (2) They were "
                "excited to explore their new neighborhood. (3) Their dog, a golden retriever named "
                "Max, loved the large backyard.\""
            ),
            "difficulty": 2,
            "choices": [
                ("Sentence 1: 'anderson' should be 'Anderson' and 'Spring' should be 'spring'.", True),
                ("Sentence 2: 'Their' should be 'They're'.", False),
                ("Sentence 3: 'Their' should be 'There'.", False),
                ("There are no errors in the passage.", False),
            ],
            "explanation": (
                "In sentence 1, 'anderson' must be capitalized because it is a proper noun (family "
                "name). 'Spring' should be lowercase because seasons are not capitalized. Sentence 2 "
                "correctly uses 'Their' (possessive -- their neighborhood). Sentence 3 correctly uses "
                "'Their' (possessive -- their dog)."
            ),
        },
        {
            "text": (
                "Read the passage and choose the answer that identifies ALL the errors correctly.\n\n"
                "\"My aunt, who is a nurse at st. luke's hospital, work the night shift every "
                "wednesday. She say the night crew are the best team she has ever work with.\""
            ),
            "difficulty": 3,
            "choices": [
                ("'st. luke's' should be 'St. Luke's'; 'work' should be 'works'; 'wednesday' should be 'Wednesday'; 'say' should be 'says'; 'work' (last) should be 'worked'.", True),
                ("Only 'st. luke's' needs to be capitalized; everything else is correct.", False),
                ("'work' should be 'works' and 'say' should be 'says'; there are no other errors.", False),
                ("'wednesday' should be 'Wednesday' and 'say' should be 'says'; there are no other errors.", False),
            ],
            "explanation": (
                "This passage contains five errors: (1) 'st. luke's' is a proper noun -- capitalize to "
                "'St. Luke's'; (2) 'work' (first) should be 'works' -- subject-verb agreement with "
                "singular 'aunt'; (3) 'wednesday' is a day of the week -- capitalize to 'Wednesday'; "
                "(4) 'say' should be 'says' -- subject-verb agreement with singular 'She'; (5) 'work' "
                "(last) should be 'worked' -- past tense for a completed experience. Only option (A) "
                "identifies all five errors."
            ),
        },
    ],
}


class Command(BaseCommand):
    help = "Seed GED RLA: Grammar & Language Conventions course"

    def handle(self, *args, **options):
        course, _ = Course.objects.update_or_create(
            slug=COURSE["slug"],
            defaults={
                "title": COURSE["title"],
                "program": COURSE["program"],
                "subject": COURSE["subject"],
                "description": COURSE["description"],
            },
        )
        course.lessons.all().delete()
        for order, (title, content) in enumerate(COURSE["lessons"], start=1):
            Lesson.objects.create(course=course, title=title, content=content, order=order)
        course.questions.all().delete()
        for item in COURSE["mcqs"]:
            q = Question.objects.create(
                course=course,
                text=item["text"],
                qtype="mcq",
                difficulty=item["difficulty"],
                explanation=item["explanation"],
            )
            for text, is_correct in item["choices"]:
                Choice.objects.create(question=q, text=text, is_correct=is_correct)
        self.stdout.write(self.style.SUCCESS(
            f"Created '{course.title}' with {len(COURSE['lessons'])} lessons and {len(COURSE['mcqs'])} questions."
        ))
