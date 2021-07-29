## `cod_convert`

Python module to convert Cockatrice `.cod` files to more a common deck format.

Current functionality is very basic and geared toward Commander decks: only the mainboard is extracted.

First install the python lxml module and its dependencies.  E.G. on ubuntu

    $ sudo apt install python3-lxml

Clone the repo into e.g. `~/src` and run

    $ python3 ~/src/cod_convert ~/.local/share/Cockatrice/Cockatrice/decks/liesa.cod
    1x Enlightened Tutor
    1x Demonic Tutor
    1x Vampiric Tutor
    1x Scheming Symmetry
    1x Diabolic Tutor
    1x Doomsday
    1x Grim Tutor
    1x Idyllic Tutor
    1x Expedition Map
    1x Weathered Wayfarer
    1x Land Tax
    1x Recruiter of the Guard
    1x Sol Ring
    1x Arcane Signet
    1x Orzhov Signet
    1x Talisman of Hierarchy
    1x Mind Stone
    1x Thought Vessel
    1x Fellwar Stone
    1x Deadly Tempest
    1x Fumigate
    1x Decree of Pain
    1x K'rrik, Son of Yawgmoth
    1x Bolas's Citadel
    1x Bond of Agony
    1x Adanto Vanguard
    1x Dark Confidant
    1x Damnable Pact
    1x Greed
    1x Erebos, God of the Dead
    1x Night's Whisper
    1x Corpse Augur
    1x Necropotence
    1x Ad Nauseam
    1x Twilight Prophet
    1x Sign in Blood
    1x Phyrexian Arena
    1x Arguel's Blood Fast
    1x Dawn of Hope
    1x Dread Presence
    1x Well of Lost Dreams
    1x Archfiend of Despair
    1x Pestilence
    1x Stunning Reversal
    1x Angel's Grace
    1x Angel of Grace
    1x Intervention Pact
    1x Platinum Angel
    1x The Book of Exalted Deeds
    1x Approach of the Second Sun
    1x Near-Death Experience
    1x Exsanguinate
    1x Mortify
    1x False Cure
    1x Swords to Plowshares
    1x Path to Exile
    1x Anguished Unmaking
    1x Font of Agonies
    1x Generous Gift
    1x Cabal Coffers
    1x Urborg, Tomb of Yawgmoth
    1x Castle Locthwain
    1x Reliquary Tower
    1x Arid Mesa
    1x Marsh Flats
    1x Prismatic Vista
    1x Godless Shrine
    1x Isolated Chapel
    1x Vault of Champions
    1x Fetid Heath
    1x Brightclimb Pathway
    1x Blacksmith's Skill
    1x Chromatic Lantern
    1x Silence
    10x Snow-Covered Plains
    10x Snow-Covered Swamp
    1x Faceless Haven
    1x Crypt Ghast
    1x Damn
    1x Command Tower
    1x Sickening Dreams

or, for convenience,

    $ python3 ~/src/cod_convert ~/.local/share/Cockatrice/Cockatrice/decks/liesa.cod | xclip -selection clipboard

to copy it to the clipboard (on linux)

    $ python3 ~/src/cod_convert ~/.local/share/Cockatrice/Cockatrice/decks/liesa.cod | pbcopy

should work on Mac.

From there you should be able to paste it into moxfield or whichever site you prefer.
