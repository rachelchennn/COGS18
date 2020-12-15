"""Module contains questions, hints, and additional statements required
to run the Fish Fact Quiz."""

from ffq_functions import Question

# Questions
Q1 = Question("Let's start with a 'trick' question. What is the correct " +
              "plural form of 'fish'?\n(a)Fishes\n(b)Fishies\n(c)Fish\n" +
              "(d)There is more than one correct answer.", 'd')

Q2 = Question("Sharks and rays are cartilaginous fishes, meaning that their " +
              "skeletons \nare made of cartilage and not bone. Which of the " +
              "following is NOT true\nabout sharks and rays?\n" +
              "(a)Their skin is made up of tiny teeth-like scales that " +
              "are structurally\nsimilar to vertebrate teeth.\n(b)Their " +
              "teeth are constantly growing and being replaced.\n(c)They " +
              "are all exclusive carnivores (meat-eaters).\n(d)They do " +
              "not have swim bladders but regulate buoyancy through " +
              "large,\nfatty livers.", 'c')

Q3 = Question("Dory from Finding Nemo is a Pacific blue tang, which is " +
              "a species of\nsurgeonfish common throughout the " +\
              "Indo-Pacific. Why is this group\nof fishes called the " +
              "surgeonfishes?\n(a)Surgeonfishes can heal the wounds of " +
              "other fishes.\n(b)Surgeonfishes have extremely sharp " +
              "modified scales that form a spine at\nthe base of their " +
              "tails.\n(c)Surgeonfishes are meticulous and careful about " +
              "the algae they graze upon.\n(d)Surgeonfishes were named " +
              "after the surgeon who first discovered them.", 'b')

Q4 = Question("Icefish live in the waters surrounding Antarctica, which " +
              "can reach temperatures\nas low as -1.9 C. Which of the " +
              "following is true about the icefish?\n(a)Icefish blood " +
              "is clear.\n(b)Icefish must constantly hunt for food to " +
              "have enough energy to warm their bodies.\n(c)Because " +
              "the water is so cold, the icefish lifespan is only 3 " +
              "months.\n(d)Icefish use pieces of kelp as sweaters to " +
              "stay warm.", 'a')

Q5 = Question("There is a huge diversity of fishes on Earth, with " +
              "lengths ranging from\nthe smallest at 7.9 mm long to the " +
              "longest growing over 110 feet long.\nWhat is the world's " +
              "largest bony fish (by weight)?\n(a)Lollipop catshark " +
              "\n(b)Giant sea bass\n(c)Sunfish\n(d)Whale shark", 'c')

Q6 = Question("Coelacanths are the oldest-known living lineage of " +
              "lobe-finned fishes,\nand along with lungfishes are more " +
              "closely related to tetrapods (such\nas reptiles and mammals) " +
              "than they are to ray-finned fishes. Which of\nthe following " +
              "is NOT true about the coelacanth?\n(a)Coelacanths are found " +
              "all around the world.\n(b)Coelacanths were considered " +
              "extinct before 1938 and found\nin the fossil record " +
              "of 400 million to 75 million years ago.\n(c)Coelacanths are able " +
              "to use electroreception to navigate around obstacles.\n(d)" +
              "Coelacanth eggs are retained in the body and embryos are given " +
              "live birth.", 'a')

Q7 = Question("This next question is not about a fish, but about a very " +
              "interesting\ninvertebrate (and one of my personal favorites!). " +
              "This deep sea\ncephalopod, which is related to squids and octopuses, " +
              "is the only known\nsurviving member of its order. It has earlike " +
              "fins that flap to propel it\nthrough the water, and can eject a cloud " +
              "of bioluminescent mucus if extremely\nagitated. What is this cephalopod's " +
              "common name?\n(a)Glass squid\n(b)Vampire squid\n(c)Flapjack octopus\n" +
              "(d)Dumbo octopus", 'b')

Q8 = Question("The deep sea is relatively understudied, despite being the " +
              "largest ecosystem\nand covering around 60% of the planet's surface. " +
              "Even though living in the\ndeep sea is extremely tough as there is no " +
              "light, little food, high pressures,\nand low temperatures, it is home " +
              "to the most abundant vertebrate on Earth.\nWhat is the common name of " +
              "this verebrate?\n(a)Lanternfish\n(b)Sardines\n(c)Swedish Fish\n(d)" +
              "Bristlemouths", 'd')

Q9 = Question("Invasive species pose serious threats to native populations as " +
              "they often do\nnot have natural predators, allowing their " +
              "populations to grow uncontrolled.\nThis invasive species, " +
              "which is native to the Indo-Pacific, is now common off\nthe " +
              "southeastern US coast after being released into the environment " +
              "by\nnegligent pet owners. What is the name of this invasive " +
              "species?\n(a)Parrotfish\n(b)Spiny seahorse\n(c)Pufferfish\n" +
              "(d)Lionfish", 'd')

Q10 = Question("Mercury is mainly introduced into the atmosphere as a byproduct of " +
               "burning coal,\nand has detrimental effects on human health including " +
               "impaired brain development\nand cognition. 80% of human exposure to " +
               "mercury comes from seafood consumption.\nWhich popular seafood item " +
               "accounts for the highest percentage of human mercury exposure?\n" +
               "(a)Shrimp\n(b)Tuna\n(c)Anchovies\n(d)Squid", 'b')


# Hints
q1_hint = "There may be more than one answer, under certain conditions."

q2_hint = "The correct answer is under the __!"

q3_hint = "You might want to be careful when handling a surgeonfish!"

q4_hint = "Colder water can carry more oxygen."

q5_hint = ("This fish spends its time at depth or at the surface where " +
           "it sunbathes.")

q6_hint = ("Not much is known about the coelacanth (despite being such " +
           "a cool fish!).")

q7_hint = "It's Halloween all year round for this cephalopod!"

q8_hint = "These fish have numerous, equally sized teeth."

q9_hint = "This fish is a voracious predator."

q10_hint = ("This seafood item ranges from being relatively inexpensive " +
            "to costing over\n$5000 a pound.")


# Additional statements corresponding to question asked
post_q1 = ("The plural form of fish is dependent on whether there are " +
           "multiple species\npresent in the group, with 'fish' being " +
           "multiple individuals of the same\nspecies and 'fishes' being " +
           "multiple individuals of multiple species.")

post_q2 = ("While most sharks are exclusive carnivores, recent studies " +
           "reveal that\nthe bonnethead shark can consume seagrass, " +
           "making it the first omnivorous shark.\nThis discovery was made " +
           "after enzymes known to break down cellulose were found\nin " +
           "the bonnethead's digestive system.")

post_q3 = ("This scalpel-like spine is also venomous and is a good defense mechanism\n" +
           "against small predators, especially since blue tangs like " +
           "to travel in schools.")

post_q4 = ("Because the waters icefish inhabit are extremely cold " +
           "and can carry more\noxygen, icefish blood does not contain " +
           "hemoglobin, which is an oxygen-carrying\nmolecule that makes " +
           "vertebrate blood red. Members of the icefish family are the\nonly " +
           "known vertebrates that lack hemoglobin as adults. Icefish blood " +
           "also contains\nantifreeze proteins, allowing these fish to " +
           "survive in the Antarctic.")

post_q5 = ("The largest species of sunfish is the bump-head sunfish, which " +
           "can weigh up to\n5 tons and grow up to 10 feet long. Sunfish can " +
           "also produce up to 300 million\neggs at once, which is more than " +
           "any other known vertebrate. Despite its large\nsize, the sunfish " +
           "was once thought to be planktonic as it appeared unable to swim\n" +
           "against currents.")

post_q6 = ("There are only two known species of coelacanth in the world, one " +
           "that occurs in\nthe waters off south and eastern Africa and the other " +
           "off Indonesia. They are\noften referred to as living fossils!")

post_q7 = ("The vampire squid's scientific name is Vampyroteuthis infernalis, " +
           "which literally\ntranslates to 'vampire squid from Hell'. Despite the " +
           "scary name, the vampire squid\nis harmless and floats around consuming " +
           "detritus (or dead organic matter) that\nsinks down from the surface waters.")

post_q8 = ("Estimates predict that there are hundreds of trillions to quadrillions " +
           "of Bristlemouth\nindividuals in the ocean. These fish are also a part of " +
           "the largest migration on\nEarth called the diel vertical migration, which " +
           "is the daily movement of deep sea\norganisms to surface waters at night to " +
           "feed and then down to depth in the day\nto escape predation.")

post_q9 = ("The lionfish has long, venomous spines, which deter predation by fish " +
           "native to the\nsoutheastern US. In some regions where lionfish populations " +
           "threaten native ecosystems,\nlionfish derbies are held as teams collect " +
           "and remove as many lionfish as they can to \ncontrol the lionfish " +
           "population. These derbies often end in lionfish tastings to \nencourage " +
           "consumption of lionfish in local restaurants.")

post_q10 = ("Despite being highly nutritious, tuna can also contain high levels of " +
            "mercury. This is\nbecause these fish feed at the top of the food web " +
            "and have extremely fast\nmetabolisms, which requires them to feed often. " +
            "Mercury concentration increases\nmoving up the food web and is not lost to " +
            "the environment as mercury prefers to\nassociate with proteins.")

# Create lists of questions, hints, and additional statements
question_list = [Q1, Q2, Q3, Q4, Q5, Q6, Q7, Q8, Q9, Q10]

hint_list = [q1_hint, q2_hint, q3_hint, q4_hint, q5_hint, q6_hint,
             q7_hint, q8_hint, q9_hint, q10_hint]

postq_list = [post_q1, post_q2, post_q3, post_q4, post_q5, post_q6,
              post_q7, post_q8, post_q9, post_q10]
