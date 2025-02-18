import os
from lib.conf import voices_dir

XTTSv2 = 'xtts'
BARK = 'bark'
VITS = 'vits'
FAIRSEQ = 'fairseq'
YOURTTS = 'yourtts'

default_tts_engine = 'xtts'
default_fine_tuned = 'internal'

# config file must always on first row
default_xtts_files = ['config.json', 'model.pth', 'vocab.json', 'ref.wav']
default_bark_files = ['coarse_2.pt']
default_fairseq_files = ['config.json', 'G_100000.pth', 'vocab.json']
default_vits_files = ['config.json', 'model_file.pth', 'language_ids.json']
default_yourtts_files = ['config.json', 'model_file.pth']

default_xtts_samplerate = 24000
default_bark_samplerate = 24000
default_vits_samplerate = 24000
default_fairseq_samplerate = 24000
default_yourtts_samplerate = 16000

# to enable_deepspeed, it must be installed manually.
# conda activate [./python_env | .\python_env]
# pip install deepspeed
# conda deactivate
tts_default_settings = {
    "temperature": 0.65,  # Natural variation without sounding robotic
    "length_penalty": 1.0,  # Encourages slightly longer phrases
    "num_beams": 1,  # More beams improve long-term coherence
    "repetition_penalty": 2.5,  # Helps prevent redundant phrasing
    "top_k": 50,  # Balanced word diversity
    "top_p": 0.8,  # Good tradeoff between diversity and coherence
    "speed": 1.0,  # Normal pace
    "enable_text_splitting": False,  # Helps with better pacing for long content (note: ab2ab is already splitting sentencess, set to True can cause more trouble)
    "use_deepspeed": False,
    "length_scale": 1.0,
    "noise_scale": 0.3
}

builtin_xtts_voices = {
    'ClaribelDervla': 'Claribel Dervla', 'DaisyStudious': 'Daisy Studious', 'GracieWise': 'Gracie Wise',
    'TammieEma': 'Tammie Ema', 'AlisonDietlinde': 'Alison Dietlinde', 'AnaFlorence': 'Ana Florence',
    'AnnmarieNele': 'Annmarie Nele', 'AsyaAnara': 'Asya Anara', 'BrendaStern': 'Brenda Stern',
    'GittaNikolina': 'Gitta Nikolina', 'HenrietteUsha': 'Henriette Usha', 'SofiaHellen': 'Sofia Hellen',
    'TammyGrit': 'Tammy Grit', 'TanjaAdelina': 'Tanja Adelina', 'VjollcaJohnnie': 'Vjollca Johnnie',
    'AndrewChipper': 'Andrew Chipper', 'BadrOdhiambo': 'Badr Odhiambo', 'DionisioSchuyler': 'Dionisio Schuyler',
    'RoystonMin': 'Royston Min', 'ViktorEka': 'Viktor Eka', 'AbrahanMack': 'Abrahan Mack',
    'AddeMichal': 'Adde Michal', 'BaldurSanjin': 'Baldur Sanjin', 'CraigGutsy': 'Craig Gutsy',
    'DamienBlack': 'Damien Black', 'GilbertoMathias': 'Gilberto Mathias', 'IlkinUrbano': 'Ilkin Urbano',
    'KazuhikoAtallah': 'Kazuhiko Atallah', 'LudvigMilivoj': 'Ludvig Milivoj', 'SuadQasim': 'Suad Qasim',
    'TorcullDiarmuid': 'Torcull Diarmuid', 'ViktorMenelaos': 'Viktor Menelaos', 'ZacharieAimilios': 'Zacharie Aimilios',
    'NovaHogarth': 'Nova Hogarth', 'MajaRuoho': 'Maja Ruoho', 'UtaObando': 'Uta Obando',
    'LidiyaSzekeres': 'Lidiya Szekeres', 'ChandraMacFarland': 'Chandra MacFarland', 'SzofiGranger': 'Szofi Granger',
    'CamillaHolmström': 'Camilla Holmström', 'LilyaStainthorpe': 'Lilya Stainthorpe', 'ZofijaKendrick': 'Zofija Kendrick',
    'NarelleMoon': 'Narelle Moon', 'BarboraMacLean': 'Barbora MacLean', 'AlexandraHisakawa': 'Alexandra Hisakawa',
    'AlmaMaría': 'Alma María', 'RosemaryOkafor': 'Rosemary Okafor', 'IgeBehringer': 'Ige Behringer',
    'FilipTraverse': 'Filip Traverse', 'DamjanChapman': 'Damjan Chapman', 'WulfCarlevaro': 'Wulf Carlevaro',
    'AaronDreschner': 'Aaron Dreschner', 'KumarDahl': 'Kumar Dahl', 'EugenioMataracı': 'Eugenio Mataracı',
    'FerranSimen': 'Ferran Simen', 'XavierHayasaka': 'Xavier Hayasaka', 'LuisMoray': 'Luis Moray',
    'MarcosRudaski': 'Marcos Rudaski'
}
builtin_yourtts_voices = {"MachinElla": "female-en-5", "ElectroMale": "male-en-2"}

models = {
    XTTSv2: {
        "internal": {
            "lang": "multi",
            "repo": "tts_models/multilingual/multi-dataset/xtts_v2",
            "sub": "",
            "voice": builtin_xtts_voices['KumarDahl'],
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "AiExplained": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/AiExplained",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"AiExplained_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "BobOdenkirk": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/BobOdenkirk",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"BobOdenkirk_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "BobRoss": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/BobRoss",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"BobRoss_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "BryanCranston": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/BryanCranston",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"BryanCranston_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "DavidAttenborough": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/DavidAttenborough",
            "voice": os.path.join(voices_dir, "eng", "elder", "male", f"DavidAttenborough_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "DeathPussInBoots": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/DeathPussInBoots",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"DeathPussInBoots_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "GhostMW2": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/GhostMW2",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"GhostMW2_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "JhonButlerASMR": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/JhonButlerASMR",
            "voice": os.path.join(voices_dir, "eng", "elder", "male", f"JhonButlerASMR_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "JhonMulaney": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/JhonMulaney",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"JhonMulaney_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "MorganFreeman": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/MorganFreeman",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"MorganFreeman_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "RainyDayHeadSpace": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/RainyDayHeadSpace",
            "voice": os.path.join(voices_dir, "eng", "elder", "male", f"RainyDayHeadSpace_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        },
        "WhisperSalemASMR": {
            "lang": "eng",
            "repo": "drewThomasson/fineTunedTTSModels",
            "sub": "xtts-v2/eng/WhisperSalemASMR",
            "voice": os.path.join(voices_dir, "eng", "adult", "male", f"WhisperSalemASMR_{default_xtts_samplerate}.wav"),
            "files": default_xtts_files,
            "samplerate": default_xtts_samplerate
        }
    },
    BARK: {
        "internal": {
            "lang": "multi",
            "repo": "tts_models/multilingual/multi-dataset/bark",
            "sub": "",
            "voice": None,
            "files": default_bark_files,
            "samplerate": default_bark_samplerate
        }
    },
    VITS: {
        "internal": {
            "lang": "multi",
            "repo": "tts_models/[lang_iso1]/[xxx]",
            "sub": {"cv/vits":["bg","cs","da","et","ga","hr","lt","lv","mt","pt","ro","sk","sl","sv"], "css10/vits":["es","fr","nl","hu","fi","ru","el","ja","zh"], "ljspeech/vits": ["en"], "thorsten/tacotron2-DDC": ["de"]},
            "voice": None,
            "files": default_vits_files,
            "samplerate": default_vits_samplerate
        }
    },
    FAIRSEQ: {
        "internal": {
            "lang": "multi",
            "repo": "tts_models/[lang]/fairseq/vits",
            "sub": "",
            "voice": None,
            "files": default_fairseq_files,
            "samplerate": default_fairseq_samplerate
        }
    },
    YOURTTS: {
        "internal": {
            "lang": "multi",
            "repo": "tts_models/multilingual/multi-dataset/your_tts",
            "sub": "",
            "voice": builtin_yourtts_voices['ElectroMale'],
            "files": default_yourtts_files,
            "samplerate": default_yourtts_samplerate
        }
    }
}