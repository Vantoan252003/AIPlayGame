"""
Visual Gesture Guide
Shows how to perform each gesture with ASCII art
"""

GESTURE_DIAGRAMS = """
════════════════════════════════════════════════════════════════════════
                        GESTURE VISUAL GUIDE
════════════════════════════════════════════════════════════════════════

1. LEAN LEFT                    2. LEAN RIGHT
   
      O                             O
     /|\\                           /|\\
     / \\                           / \\
    ↙                                 ↘
  LEAN LEFT                       LEAN RIGHT
  (Move body left)               (Move body right)

════════════════════════════════════════════════════════════════════════

3. JUMP                         4. CROUCH

       \\O/                         _O_
        |                          /|\\
       / \\                         |_|
       ↑                            ↓
   ARMS UP                      SQUAT DOWN
   (Raise hands)                (Lower body)

════════════════════════════════════════════════════════════════════════

5. HANDS JOINED                 6. LEFT PUNCH

        O                           O
       🤝                         ═|―
       /|\\                         /|
       / \\                         / \\
    HANDS TOGETHER              ARM EXTENDED LEFT
    (Wrists touch)              (Extend left arm)

════════════════════════════════════════════════════════════════════════

7. RIGHT PUNCH                  8. LEFT KICK

        O                           \\O
       ―|═                          |
        |\\                          |
       / \\                          ═
  ARM EXTENDED RIGHT             LEG RAISED LEFT
  (Extend right arm)             (Lift left leg)

════════════════════════════════════════════════════════════════════════

9. RIGHT KICK                   10. BLOCK

        O/                          \\|/
        |                            O
        |                           /|\\
        ═                           / \\
   LEG RAISED RIGHT              ARMS UP GUARD
   (Lift right leg)              (Protect face)

════════════════════════════════════════════════════════════════════════

11. LEFT UPPERCUT               12. RIGHT UPPERCUT

       \\O                           O/
        |⬆                          ⬆|
       /|                            |\\
       / \\                           / \\
   LEFT FIST UP                  RIGHT FIST UP
   (Raise left fist)             (Raise right fist)

════════════════════════════════════════════════════════════════════════

                        BODY POSITION GUIDE

NEUTRAL STANCE (Starting Position):
              
              O          ← Head
             /|\\         ← Arms relaxed
              |          ← Torso straight
             / \\         ← Legs shoulder-width

Always return to this position between gestures!

════════════════════════════════════════════════════════════════════════

                        CAMERA VIEW ZONES

    ┌─────────────────────────────────────┐
    │         CAMERA FIELD OF VIEW        │
    │                                     │
    │  ┌─────────────────────────────┐   │
    │  │                             │   │
    │  │    MUST BE IN THIS FRAME    │   │
    │  │                             │   │
    │  │           \\O/               │   │ ← Full body
    │  │            |                │   │   must be
    │  │           / \\               │   │   visible
    │  │                             │   │
    │  └─────────────────────────────┘   │
    │                                     │
    └─────────────────────────────────────┘
    
    Distance: 2-2.5 meters (6-8 feet)

════════════════════════════════════════════════════════════════════════

                    DETECTION ZONES (Top View)

              LEFT    CENTER    RIGHT
            
               |        |        |
               |   ←    o    →   |
               |        |        |
               
            15% margin each side
            
    • Stand at 'o' = CENTER
    • Lean left past left line = LEFT
    • Lean right past right line = RIGHT

════════════════════════════════════════════════════════════════════════

                    COMMON MISTAKES ❌ vs CORRECT ✓

PUNCH:
❌ Arm bent                    ✓ Arm straight forward
   
   O                              O
  /|―                           ―|―
  / \\                            / \\
  
────────────────────────────────────────────────────────────

KICK:
❌ Leg barely raised           ✓ Knee above hip

   O                              \\O
  /|\\                             |
  /―\\                             |
                                   ―
                                   
────────────────────────────────────────────────────────────

BLOCK:
❌ Arms down                   ✓ Arms up to face

   O                             \\|/
  /|\\                             O
  / \\                            /|\\
                                  / \\

────────────────────────────────────────────────────────────

HANDS JOINED:
❌ Hands far apart             ✓ Wrists touching

   O                              O
  /―\\                            🤝
  / \\                            / \\

════════════════════════════════════════════════════════════════════════

                        TIMING DIAGRAM

Frame:  1   2   3   4   5   6   7   8   9  10  11  12  13  14  15
        │   │   │   │   │   │   │   │   │   │   │   │   │   │   │
Punch:  ═══════════════►                                         
        │ Detected!   │◄───── Cooldown (15 frames) ─────►│
                                                          │
Next:                                                  Can punch
                                                        again!

• Gesture must be clear for detection
• After detection, cooldown prevents spam
• Return to neutral during cooldown
• Wait for cooldown to complete before next action

════════════════════════════════════════════════════════════════════════

                    SKELETON LANDMARK POINTS

              0 (Nose)
              │
        11 ──┼── 12     (Shoulders)
              │
        13 ──┼── 14     (Elbows)
              │
        15 ──┼── 16     (Wrists)
              │
        23 ──┼── 24     (Hips)
              │
        25 ──┼── 26     (Knees)
              │
        27 ──┼── 28     (Ankles)

These points are tracked by MediaPipe
Make sure all visible in camera!

════════════════════════════════════════════════════════════════════════

                        PRACTICE ROUTINE

Step 1: BASIC MOVEMENTS (2 minutes)
  • Lean left and right
  • Jump (arms up)
  • Crouch (squat)
  • Join hands

Step 2: FIGHTING MOVES (3 minutes)
  • Left punch
  • Right punch
  • Left kick
  • Right kick

Step 3: ADVANCED MOVES (3 minutes)
  • Block
  • Left uppercut
  • Right uppercut
  • Combination moves

Step 4: PRACTICE WITH DEMO (5 minutes)
  • Run: bash run_demo_actions.sh
  • Try each gesture
  • Watch detection feedback
  • Adjust movements

Step 5: PLAY! (∞ minutes)
  • Run: bash run_universal.sh
  • Select your game
  • Have fun!

════════════════════════════════════════════════════════════════════════

                        QUICK TIPS

💡 Make it BIG: Exaggerate all movements
💡 Be CLEAR: Hold each gesture for 2-3 frames
💡 Stay CENTERED: Keep body in frame center
💡 Good LIGHT: Bright, even lighting
💡 Plain BACKGROUND: Avoid clutter
💡 Practice FIRST: Use demo mode
💡 Have FUN: Enjoy the game!

════════════════════════════════════════════════════════════════════════
"""

if __name__ == "__main__":
    print(GESTURE_DIAGRAMS)
