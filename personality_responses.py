import random

PERSONALITY_RESPONSES = {
    "Gen Z": [
        "Bro, that's lit 🔥",
        "Deadass? 😂",
        "You just gave main character energy.",
        "Slayyyy, not gonna lie.",
        "Lowkey feel that fr fr."
    ],
    "Funny": [
        "I'm not saying I'm Batman, but you've never seen us in a room together.",
        "I used to think I was indecisive, but now I'm not too sure.",
        "My imaginary friend says you have serious issues.",
        "You're the reason I check behind the shower curtain.",
        "I'm multitasking: I can listen, ignore, and forget at the same time."
    ],
    "Formal": [
        "Thank you for your input. I will consider it carefully.",
        "It is my pleasure to assist you.",
        "Could you please clarify your last statement?",
        "I acknowledge your perspective and respect it.",
        "Let us proceed in an orderly and respectful manner."
    ],
    "Sarcastic": [
        "Oh wow, what an *original* idea. Groundbreaking!",
        "Sure, because that’s never gone wrong before.",
        "Well aren’t you just a genius in disguise.",
        "Fantastic! Another thing I didn’t ask for.",
        "Right, because I totally have time for that."
    ],
    "Motivational": [
        "You’re stronger than you think. Keep going!",
        "Every day is a new beginning. Let’s go!",
        "Push yourself, because no one else is going to do it for you.",
        "Small steps lead to big results.",
        "Your future self will thank you!"
    ],
    "Philosophical": [
        "What is truth, if not perspective shaped by time?",
        "The unexamined life is not worth living – Socrates.",
        "You are not just a drop in the ocean; you are the entire ocean in a drop.",
        "We live in a world of questions, not answers.",
        "To know others is intelligence, to know yourself is true wisdom."
    ],
    "Poetic": [
        "Like moonlight dancing on silent seas, your words echo softly.",
        "In the garden of thought, your question blooms beautifully.",
        "Even stars need the dark to shine. So do you.",
        "The wind carries whispers only the soul understands.",
        "Hope floats, even in the deepest sorrow."
    ],
    "Savage": [
        "You're not useless—you can always serve as a bad example.",
        "Your secrets are safe with me. I never even listen.",
        "You bring everyone so much joy… when you leave the room.",
        "You're the reason the gene pool needs a lifeguard.",
        "Mirror: you dropped this L."
    ],
    "Wholesome": [
        "I'm so proud of you 💖",
        "You’re doing amazing, sweetie!",
        "Sending you a big warm hug!",
        "You matter. Always.",
        "The world is better with you in it 😊"
    ],
    "Creepy": [
        "I see you… even when you think I don’t.",
        "Your walls whisper at night. Do you hear them?",
        "The shadows know your name.",
        "You're never really alone. Ever.",
        "I remember your dreams… even the forgotten ones."
    ],
    "Techie": [
        "Sounds like a solid 404 brain error.",
        "I'd debug that thought if I were you.",
        "Just like JavaScript, this convo has no type.",
        "You’ve got more bugs than my last build.",
        "Ctrl + Alt + Delete your drama, please."
    ],
    "Romantic": [
        "Every moment with you feels like poetry.",
        "Are you a spark? Because you light up my world.",
        "You must be gravity because I’m falling for you.",
        "Even in a thousand lifetimes, I’d still choose you.",
        "Your smile rewrites the code of my heart."
    ],
    "Rude": [
        "Is that your brain talking or just background noise?",
        "That idea could use some... deletion.",
        "You must be the reason we have warning labels.",
        "Were you born this annoying or is it a talent?",
        "You're the human version of a software crash."
    ],
    "Minimalist": [
        "Clear. Direct. Done.",
        "Only what matters. Nothing more.",
        "Silence is also a statement.",
        "Less talk. More meaning.",
        "Keep it clean. Keep it sharp."
    ],
    "Meme Lord": [
        "Bruh moment 🫠",
        "When life gives you lemons, make memes.",
        "I understood that reference. *Insert MCU GIF*",
        "One does not simply ignore this chat.",
        "This message slaps harder than Will Smith."
    ],
    "Anime Fan": [
        "Believe it! 🌀 (Naruto style)",
        "This convo has more filler than a shonen arc.",
        "You have my respect, senpai.",
        "In the name of friendship and honor, I reply!",
        "Even Levi would raise an eyebrow at this."
    ],
    "Spiritual": [
        "The universe listens to every intention.",
        "Close your eyes and breathe. You are whole.",
        "Karma is always watching.",
        "Awaken the light within.",
        "Your journey is sacred."
    ],
    "Old Soul": [
        "In my day, we had real conversations.",
        "The best wisdom comes from silence.",
        "Young minds rush; wise ones reflect.",
        "Write letters, not texts.",
        "I’ve lived through seven versions of Windows."
    ],
    "Desi Vibe": [
        "Kya baat hai yaar! Full paisa vasool 💥",
        "Seedha dil se bola tune!",
        "Arey waah, mast response!",
        "Biryani jaisi baat ki tune.",
        "Aaj toh full josh mein lag raha tu!"
    ]
}

def get_response(personality, user_input):
    responses = PERSONALITY_RESPONSES.get(personality)
    if not responses:
        return "Oops! I don’t have a response for that personality yet."
    return random.choice(responses)
