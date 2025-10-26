
ENDLESS_RUNNER_PROFILE = {
    'name': 'Endless Runner (Subway Surfers, Temple Run)',
    'type': 'endless_runner',
    'controls': {
        'left': 'left',
        'right': 'right',
        'jump': 'up',
        'crouch': 'down',
        'start': 'space',
    },
    'gestures': {
        'left_right': True,
        'jump_crouch': True,
        'hands_joined': True,
    },
    'settings': {
        'game_start_click': (1300, 800),
        'num_frames_to_start': 10,
        'hands_joined_threshold': 130,
    }
}

ACTION_GAME_PROFILE = {
    'name': 'Action/Fighting Game',
    'type': 'action',
    'controls': {
        'punch': 'j',
        'left': 'a',
        'right': 'd',
        'jump': 'k',
        'crouch': 'i',
    },
    'gestures': {
        'punch': True,
        'left_right': True,
        'jump_crouch': True,
    },
    'settings': {
        'cooldown_frames': 3,
        'punch_threshold': 0.08,
    }
}

# ========================= PLATFORMER GAMES =========================

PLATFORMER_PROFILE = {
    'name': 'Platformer Game',
    'type': 'platformer',
    'controls': {
        'left': 'left',
        'right': 'right',
        'jump': 'space',
        'crouch': 'down',
        'run': 'shift',
    },
    'gestures': {
        'left_right': True,
        'jump_crouch': True,
        'hands_joined': True,
    },
    'settings': {
        'game_start_click': None,
        'num_frames_to_start': 8,
    }
}

RACING_PROFILE = {
    'name': 'Racing Game',
    'type': 'racing',
    'controls': {
        'left': 'left',
        'right': 'right',
        'accelerate': 'up',
        'brake': 'down',
        'boost': 'shift',
    },
    'gestures': {
        'left_right': True,
        'jump_crouch': True,
        'hands_joined': True,
    },
    'settings': {
        'game_start_click': None,
        'num_frames_to_start': 10,
        'hands_joined_threshold': 130,
    }
}

GAME_PROFILES = {
    '1': ENDLESS_RUNNER_PROFILE,
    '2': ACTION_GAME_PROFILE,
    '3': PLATFORMER_PROFILE,
    '4': RACING_PROFILE,
}

GAME_MENU = """
╔══════════════════════════════════════════════════════════════════╗
║                    🎮 CHON GAME 🎮                               ║
╚══════════════════════════════════════════════════════════════════╝

  1️⃣  Endless Runner (Subway Surfers, Temple Run)
      Nghieng trai/phai, Nhay, Cui
      
  2️⃣  Action/Fighting Game
      Dam (duoi thang tay), Di chuyen (nghieng), Nhay/Cui
      Phim: J (dam), A/D (trai/phai), K (nhay), I (cui)
      
  3️⃣  Platformer (Mario, Celeste)
      Trai/Phai, Nhay, Cui, Chay (cham 2 tay)
      
  4️⃣  Racing Game
      Re (nghieng), Tang/Giam toc, Boost (cham 2 tay)

  0️⃣  Thoat

╔══════════════════════════════════════════════════════════════════╗
"""

# ========================= RACING GAMES =========================

RACING_PROFILE = {
    'name': 'Racing Game',
    'type': 'racing',
    'controls': {
        'left': 'left',           # Steer left
        'right': 'right',         # Steer right
        'accelerate': 'up',       # Jump = Accelerate
        'brake': 'down',          # Crouch = Brake
        'boost': 'shift',         # Hands joined = Boost
    },
    'gestures': {
        'left_right': True,
        'jump_crouch': True,
        'hands_joined': True,
    },
    'settings': {
        'game_start_click': None,
        'num_frames_to_start': 10,
        'hands_joined_threshold': 130,
    }
}

# ========================= GAME PROFILES REGISTRY =========================

GAME_PROFILES = {
    '1': ENDLESS_RUNNER_PROFILE,
    '2': ACTION_GAME_PROFILE,
    '3': PLATFORMER_PROFILE,
    '4': RACING_PROFILE,
}

# Menu display
GAME_MENU = """
╔══════════════════════════════════════════════════════════════════╗
║                    🎮 GAME SELECTOR MENU 🎮                      ║
╚══════════════════════════════════════════════════════════════════╝

Chon the loai game:

  1️⃣  Endless Runner (Subway Surfers, Temple Run)

      
  2️⃣  Action/Fighting Game (Simple)

      
  3️⃣  Platformer (Mario, Celeste)
      
  4️⃣  Racing Game (Need for Speed, Asphalt)

  
  0️⃣  Exit

╔══════════════════════════════════════════════════════════════════╗
"""

