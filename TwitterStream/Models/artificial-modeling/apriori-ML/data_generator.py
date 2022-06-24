
import numpy as np
from scipy import spatial

contexts = {
'Person':27480,
'TV Shows':7528,
'Brand Vertical':4331,
'Entities [Entity Service]':3714,
'Brand Category':3492,
'Interests and Hobbies Vertical':2597,
'Ongoing News Story':2290,
'Brand':2131,
'Events [Entity Service]':1610,
'Interests and Hobbies Category':1416,
'Video Game':1070,
'Music Genre':900,
'States':887,
'Multimedia Franchise':868,
'Cities':698,
'Interests and Hobbies':693,
'Political Body':627,
'Sport':588,
'Sports Team':551,
'Sports Event':528,
'Fan Community':515,
'Movie':496,
'Music Album':368,
'Reoccurring Trends':284}

testing_contexts = ['Video Game', 'Music Genre', 'Citites', 'Sport']

dict_words = {}
# Cambridge 
'''
dict_words['Video Game'] = {
    'definition': ["a", "game", "in", "which", "the", "player", "controls", "moving", "pictures", "on", "a", "screen", "by", "pushing", "buttons", "His", "new", "video", "game", "is", "apparently", "selling", "like", "hot", "cakes", "", "He", "gets", "really", "hyped", "up", "when", "he", "s", "playing", "video", "games", "", "That", "video", "game", "is", "really", "neat", "", "The", "problem", "with", "video", "games", "is", "that", "they", "re", "addictive", "", "a", "game", "in", "which", "the", "player", "controls", "moving", "pictures", "on", "a", "television", "screen", "by", "pressing", "buttons", "or", "moving", "a", "short", "handle", "", "The", "best", "video", "games", "involve", "using", "your", "imagination", "to", "solve", "problems", "", "If", "you", "re", "going", "to", "completely", "change", "the", "tone", "and", "concept", "from", "the", "video", "game", "", "why", "even", "base", "it", "on", "the", "franchise", "", "I", "m", "pretty", "sure", "this", "movie", "will", "go", "down", "as", "just", "another", "bad", "video", "game", "movie", "", "Nobody", "else", "s", "daughter", "is", "in", "that", "video", "game", "", "If", "you", "like", "your", "history", "to", "be", "accurate", "", "this", "isn", "t", "your", "kind", "of", "video", "game", "", "But", "it", "s", "the", "near", "film", "quality", "cutscenes", "that", "steal", "the", "show", "and", "almost", "make", "you", "forget", "you", "re", "playing", "a", "video", "game", "", "Is", "there", "such", "a", "thing", "as", "video", "game", "addiction", "", "It", "is", "the", "highest", "grossing", "video", "game", "of", "all", "time", "", "With", "those", "kinds", "of", "reasoning", "powers", "", "kids", "can", "handle", "a", "video", "game", "that", "doesn", "t", "even", "claim", "to", "be", "real", "", "November", "is", "one", "of", "the", "two", "most", "important", "months", "for", "sales", "in", "the", "video", "game", "industry", "", "and", "this", "year", "s", "was", "a", "big", "one", "", "One", "of", "the", "coolest", "bits", "of", "video", "game", "technology", "to", "come", "to", "gaming", "in", "2011", "doesn", "t", "even", "require", "electricity", "to", "operate", "", "Like", "any", "great", "video", "game", "", "her", "music", "is", "imaginative", "", "immersive", "and", "highly", "addictive", "", "By", "further", "distancing", "us", "from", "the", "battlefield", "", "they", "ll", "turn", "war", "into", "a", "very", "real", "video", "game", "", "The", "document", "offers", "a", "specific", "example", "of", "a", "video", "game", "blogger", "who", "gets", "a", "free", "game", "system", "that", "he", "later", "talks", "about", "on", "his", "blog", "", "Some", "are", "dismissing", "the", "video", "as", "a", "marketing", "campaign", "for", "a", "video", "game", "or", "movie", "and", "not", "a", "real", "threat", "", "The", "video", "game", "provides", "the", "distraction", "that", "overwhelms", "the", "senses", "and", "diverts", "the", "brain", "s", "attention", "away", "from", "processing", "the", "pain", "signals"],
    'related': ["acrostic"," air hockey"," bagatelle"," beer pong"," bingo"," boomerang"," bran tub"," buildering"," bungee"," bungee jump"," bungee jumping"," cage diving"," charade"," Chinese puzzle"," coloring book"," computer game"," crossword"," cryptic crossword"," cycling"," dice"," die"," domino"," draw"," drinking game"," e-sports"," egg-and-spoon race"," escape room"," fell running"," fetch"," footgolf"," free running"," freestyle football"," Frisbee"," game console"," gamification"," gaming"," glassing"," go"," Hacky Sack"," hangman"," hoopla"," horseshoe"," in-game"," inline"," inline skate"," inline skating"," jigsaw"," jigsaw puzzle"," juggling"," jump rope"," keepy-uppy"," kite"," korfball"," LARP"," LARPer"," level"," level sth up"," level up"," lotto"," magnet fishing"," maze"," noughts and crosses"," NPC"," origami"," paintball"," paintballing"," parkour"," parlor game"," people watching"," pinball"," pinball machine"," Pokémon"," pop quiz"," power-up"," pub quiz"," puzzle"," quidditch"," quizzing"," quoits"," raffle"," resistance training"," ringtoss"," role-playing game"," roller skate"," roller-skating"," Rollerblade"," rounders"," RPG"," scavenger hunt"," screen time"," shoot-em-up"," shooter"," skin"," skip"," skipping rope"," social game"," softball"," stoop ball"," story mode"," subworld"," sudoku"," table football"," tabletop"," tailgating"," three-legged race"," tic-tac-toe"," tiddlywink"," tiddlywinks"," touch football"," trail running"," treasure hunt"," tug of war"," video game"," Wii"," word search"," yo-yoing"," zorbing"]
}
'''
dict_words['Video Game'] = {
    'subject': ['Video Game'],
    'synonymous': ["computer game", "Nintendo", "Playstation", "Xbox", "computerized game", "electronic game"],
    'definition': ["any","of","various","interactive","games","played","using","a","specialized","electronic","gaming","device","or","a","computer","or","mobile","device","and","a","television","or","other","display","screen,","along","with","a","means","to","control","graphic","images","any","of","various","games","played","using","a","microchip-controlled","device,","as","an","arcade","machine","or","handheld","toy"],
    'definition_synonymous': ["all", "each", "either", "several", "a bit", "a little", "each and every", "in general", "part of", "whatever", "about", "appertaining to", "appropriate to", "as concerns", "as regards", "attributed to", "away from", "based on", "belonging to", "characterized by", "coming from", "concerning", "connected with", "consisting of", "containing", "epithetical", "going from", "in reference to", "in regard to", "like", "made from", "out from", "out of", "peculiar to", "pertaining to", "proceeding from", "referring to", "regarding", "related to", "showing", "assorted", "different", "discrete", "disparate", "distinct", "diverse", "diversified", "individual", "numerous", "separate", "sundry", "varied", "all manner of", "changeable", "changing", "distinctive", "heterogeneous", "legion", "manifold", "many", "many-sided", "multifarious", "multitudinal", "multitudinous", "omnifarious", "peculiar", "populous", "several", "unalike", "unequal", "unlike", "variant", "variegated", "bilateral", "collective", "reciprocal", "associated", "communal", "conjoint", "conjunct", "connected", "convertible", "correlative", "dependent", "give-and-take", "given and taken", "interchangeable", "interchanged", "interdependent", "intermutual", "joint", "partaken", "participated", "public", "reciprocated", "related", "requited", "respective", "returned", "two-sided", "united", "contest", "drill", "events", "exercises", "practice", "recreation", "workout", "baited", "bamboozled", "betrayed", "conned", "culled", "duped", "fooled", "gulled", "had", "hoaxed", "hoodwinked", "lured", "snared", "taken", "trapped", "victimized", "accepting", "adopting", "applying", "employing", "practicing", "proving", "testing", "working", "an", "one", "functional", "particular", "specially designed", "computerized", "anodic", "autoelectronic", "cathodic", "photoelectronic", "thermionic", "voltaic", "action", "speculation", "staking", "laying odds", "accessory", "apparatus", "appliance", "equipment", "gadget", "gear", "machine", "material", "mechanism", "agent", "arrangement", "article", "construction", "contraption", "contrivance", "creation", "doohickey", "expedient", "gimmick", "implement", "invention", "makeshift", "means", "medium", "outfit", "resort", "resource", "rigging", "shift", "tackle", "thingamabob", "utensil", "whatchamacallit", "whatnot", "Rube Goldberg invention", "whatsit", "CPU", "PC", "abacus", "analog", "brain", "calculator", "clone", "laptop", "mac", "mainframe", "microcomputer", "mini", "minicomputer", "adding machine", "artificial intelligence", "data processor", "digital", "electronic brain", "micro", "number cruncher", "personal computer", "thinking machine", "ambulatory", "fluid", "free", "itinerant", "liquid", "locomotive", "migrant", "motile", "peripatetic", "portable", "roving", "wandering", "adaptable", "changeable", "loose", "migratory", "motorized", "moving", "mutable", "nomadic", "roaming", "unsettled", "unstable", "unstationary", "unsteadfast", "unsteady", "versatile", "TV set", "audio", "box", "station", "video", "TV", "baby-sitter", "eye", "receiver", "telly", "tube", "boob tube", "idiot box", "small screen", "vid", "act", "array", "demonstration", "example", "exhibit", "parade", "presentation", "affectation", "arrangement", "blaze", "bravura", "dash", "exhibition", "expo", "exposition", "exposure", "fanfare", "flourish", "frame-up", "frippery", "front", "layout", "manifestation", "ostentation", "ostentatiousness", "pageant", "panorama", "pedantry", "pomp", "pretension", "pretentiousness", "revelation", "sample", "scheme", "shine", "showboat", "splash", "splendor", "splurge", "spread", "unfolding", "vanity", "arrayal", "for show", "grandstand play", "cover", "curtain", "net", "awning", "canopy", "cloak", "concealment", "covering", "divider", "envelope", "guard", "hedge", "mantle", "mask", "partition", "security", "shade", "shelter", "shield", "shroud", "veil", "aid", "channel", "equipment", "factor", "instrument", "measure", "mechanism", "medium", "mode", "power", "process", "route", "step", "system", "tactic", "technique", "vehicle", "agency", "agent", "apparatus", "auspices", "avenue", "course", "dodge", "expedient", "fashion", "gimmick", "instrumentality", "instrumentation", "intermediary", "machinery", "manner", "ministry", "organ", "organization", "paraphernalia", "path", "road", "trick", "modus operandi", "stepping-stone", "ways and means", "authority", "curb", "discipline", "domination", "force", "government", "jurisdiction", "management", "oversight", "regulation", "restraint", "restriction", "rule", "supervision", "ascendancy", "bridle", "charge", "check", "clout", "containment", "determination", "direction", "dominion", "guidance", "juice", "limitation", "manipulation", "might", "predomination", "qualification", "regimentation", "ropes", "strings", "subjection", "subordination", "superintendence", "supremacy", "sway", "weight", "driver seat", "inside track", "upper hand", "wire pulling", "concrete", "stirring", "striking", "telling", "colorful", "compelling", "comprehensible", "convincing", "definite", "descriptive", "detailed", "distinct", "eloquent", "expressive", "figurative", "forcible", "illustrative", "incisive", "intelligible", "lively", "lucid", "moving", "perspicuous", "picturesque", "precise", "realistic", "strong", "unequivocal", "vivid", "appearance", "copy", "drawing", "figure", "form", "icon", "illustration", "likeness", "model", "photograph", "picture", "portrait", "statue", "angel", "carbon", "double", "effigy", "equal", "equivalent", "facsimile", "idol", "match", "photocopy", "reflection", "replica", "reproduction", "similitude", "simulacrum", "carbon copy", "carved figure", "chip off old block", "dead ringer", "simulacre", "spitting image", "chip", "circuitry", "microprocessor", "silicon chip", "IC", "computer chip", "logic circuit", "microcircuit", "microelectronics", "microprocessor chip", "semiconductor chip", "transputer", "composed", "contained", "disciplined", "guarded", "restrained", "calm", "cool", "inhibited", "self-controlled", "self-restrained", "under control", "unflappable", "gallery", "mall", "walkway", "cloister", "colonnade", "loggia", "passageway", "piazza", "portico", "stoa", "apparatus", "appliance", "automobile", "engine", "gadget", "instrument", "motor", "tool", "vehicle", "automaton", "computer", "contraption", "contrivance", "implement", "mechanism", "robot", "thingamabob", "widget", "constraint", "grasp", "restraint", "anchor", "brace", "catch", "cinch", "cincture", "clamp", "clamping", "clench", "clinch", "clutch", "coercion", "crushing", "duress", "enclosing", "enclosure", "fastening", "fixing", "grapnel", "grapple", "gripe", "handclasp", "handgrip", "handshake", "hold", "hook", "ligature", "lug", "purchase", "snatch", "squeeze", "strength", "tenure", "vise", "wrench", "doll", "plaything", "trinket", "bauble", "curio", "game", "knickknack", "novelty", "trifle"]
}
weights = {'subject':2**3, 'synonymous':2**2, 'definition':2**1, 'definition_synonymous':2**0}

video_game_words = []
for word_list in dict_words['Video Game'].values():
    video_game_words += word_list
video_game_words = set(video_game_words)

#print(video_game_words)


embeddings_dict={}
with open('C:/Users/marci/Documents/Portfolio/TwitterClassification/TwitterStream/data/glove.6B.50d.txt','rb') as f:
    for line in f:
        values = line.split()
        word = values[0]
        vector = np.asarray(values[1:], "float32")
        embeddings_dict[word] = vector

print(embeddings_dict[b'test'])
def find_closest_embeddings(embedding):
   return sorted(embeddings_dict.keys(), key=lambda word:
       spatial.distance.euclidean(embeddings_dict[word], embedding)
    )

#print(find_closest_embeddings(b'game')[:100])

