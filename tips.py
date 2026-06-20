import streamlit as st
import random
import pyjokes
import json
import string
import base64
import os

st.markdown("""
<h1 style='text-align:center;color:white;'>
🤖 THE TIPS AI
</h1>
""", unsafe_allow_html=True)

st.write("Created by Sommay Singh")

option = st.selectbox(
    "Choose a feature",
    [   
        "About Creator",
        "storage memory",
        "Counter",
        "Calculator",
        "Guessing Game",
        "Joke",
        "Open web",
        "ABCD",
        "Password Generator",
        "Dice Roller",
        "Coin Toss" 
        
    ]
)

# Calculator
if option == "Calculator":
    st.subheader("🧮 Calculator")
    num1 = st.number_input("First Number")
    op = st.selectbox(
        "Choose Operator",
        ["+", "-", "*", "/", "%"]
    )
    num2 = st.number_input("Second Number")

    if st.button("Calculate"):
        try:
            if op == "+":
                answer = num1 + num2
            elif op == "-":
                answer = num1 - num2
            elif op == "*":
                answer = num1 * num2
            elif op == "/":
                answer = num1 / num2
            elif op == "%":
                answer = num1 % num2
            st.success(f"Answer = {answer}")
        except:
            st.error("Calculation Error")

# Joke
import gtts
if option == "Joke":
    joke_lang = st.selectbox(
        "What language do you want to hear jokes in?",
        ["English", "Hindi"]
    )
    
    if joke_lang == "English":
        st.subheader("😂 Joke Generator")
        if st.button("Tell Me A Joke"):
            eng_joke = pyjokes.get_joke()
            st.info(eng_joke)

    if joke_lang == "Hindi":
        st.subheader("😂 Hinglish Joke Generator")
           
        hindi_jokes = [
                "Teacher: Sommay, agar tumhare paas 4 kele hain aur tumne 2 apni behen ko de diye, toh tumhare paas kya bacha?\n\nSommay: Ek ghante tak uski chikh-pukar aur rona! 🍌😂",
                "PTM ka Sach: Jab Papa class mein teacher ke samne baithte hain, toh lagta hai jaise CID ke samne koi mujrim baitha ho aur abhi thappad padne wala hai! 👨‍✈️",
                "Teacher: Akash, Akbar ne kab tak raaj kiya tha ? Akash: Ma'am, page number 45 se lekar page number 52 tak! 📖",
                "Mummy: PTM ka result kaisa raha? Beta: Mummy, teacher bol rahi thi ki aapka beta bohot 'Unique' hai, sabse alag hi chalta hai! 🏃\u200d♂️",
                "Teacher: 15 mahine ka naam batao? Pappu: Ma'am, Jan-Feb-March... aur baaki ke 3 mahine garmi ki chhuttiyan! ☀️",
                "Teacher: Agar tumhare paas 10 chocolates hain aur tumne 3 apne dost ko de diye, toh tumhare paas kya bacha?\n\nPappu: Ma'am, 7 chocolates! Aur ek dosti ka rishta! 🍫🤝",
                "Student: Ma'am, kya aap mujhe us baat ki saza dengi jo maine nahi ki? Teacher: Bilkul nahi beta! Student: Achha ma'am, toh maine aaj homework nahi kiya hai! 📝💨",
                "Exam Time: Jab pure hall mein sirf ek hi aawaaz aaye—'Ma'am, extra sheet please!'—toh man karta hai us bache ki sheet lekar usme aeroplane bana dein! ✈️",
                "Teacher: Kal kyun nahi aaye? Pappu: Ma'am, kal raste mein ek board laga tha 'Aage school hai, dhyan se chalien', isiliye main dhyan se wapas ghar chala gaya! 🚸",
                "History Class: Padha rahe hain 500 saal purani ladai, aur mera dimaag soch raha hai ki aaj canteen mein samosa garam milega ya nahi! 🥟",
                "Dost ka logic: 'Bhai, agar main fail hua toh akela fail hunga, par agar tu fail hua toh dosti ka record banega!' 🤜🤛",
                "Mummy: Sommay, dukan se jaakar chawal le aa, aur agar dukan par ande milein toh 6 le aana.\n\nSommay (Coder Brain): Dukan par ande mile, toh chawal ki jagah 6 chawal ke packet le aaya!\nMummy: Yeh kya hai?!\nSommay: Mummy, coding logic! if eggs_found == True: buy(6) 🥚🤦\u200d♂️",
                "Apun ka Laptop: Jab main Minecraft chala raha hota hoon aur piche browser mein 10 tabs khul jayein, toh laptop ki aawaaz aisi aati hai jaise helicopter take-off karne wala ho! 🛸",
                "SyntaxError: invalid syntax. Me: Bhai, galti kahan hai bas itna bata de, pure code par laal patti maar kar dulaar kyun dikha raha hai? 🔴",
                "Papa: Beta, tera ye 'India's third AI' kya kya kar sakta hai? Sommay: Papa, ye har mushkil sawal ka jawab de sakta hai! Papa: Isse pooch kal KV Khichripur mein chhutti hai kya? Agar nahi hui toh subah uthna padega! 🏫",
                "Coder Life: 2 ghante code likha, 4 ghante error theek kiya, aur aakhiri mein pata chala ki ek space ki galti thi! 🌌",
                "Teacher: Sommay, agar koi chor tumhare ghar se saari dahi chura le jaye, toh tum kya karoge? Sommay: Ma'am, main dukan se dahi lane ke jhanjhat se bach jaunga aur Streamlit cloud par code deploy karunga! 🍦💻",
                "Pappu: Papa, aaj hamare KV Khichripur mein sabse bada jhoot bola gaya. Papa: Kya? Pappu: Teacher ne kaha ki 'Sabhi bachhe mere liye ek barabar hain', aur agle hi second roll no. 1 ko poore 10 marks de diye! 📝😂",
                "Teacher: Jo padhega wo badhega, jo nahi padhega wo kya korea? Akash: Ma'am, wo backbench par baith kar aaram se aaloo ka paratha khayega! 🥞",
                "Math Exam: Sawaal tha—'Prove that X = Y.' Me: Maine likha—'Bhai, jab dono aapas mein barabar hain toh beech mein mujhe kyun la rahe ho, khud hi samajh lo!' 🤷‍♂️",
                "Teacher: Kal sab log apna homework lekar aana, nahi toh class ke bahar 'Murga' banna padega. Backbencher: Ma'am, roti sath mein lani hai ya canteen mein milegi? 🍗",
                "Mummy: Sommay, tera 7th class ka maths ka result kaisa raha? Sommay: Mummy, maths ka toh pata nahi par meri typing speed 40 WPM ho gayi hai coding se! ⌨️",
                "Teacher: Akbar ne Buland Darwaza kyun banwaya tha? Pappu: Ma'am, kyunki uske paas dukan se dahi lane ka koi naya robot nahi tha! 🚪",
                "Dost 1: Bhai, kal physics ke paper mein kya likha? Dost 2: Maine poora paper khali chhod diya! Dost 1: O teri! Maine bhi khali chhod diya, teacher sochegi humne cheating ki hai! 📄🤣",
                "Teacher: Class mein itna shor kyun ho raha hai? Student: Ma'am, wo topper bachha achanak fail ho gaya, toh sab log khushi mein party kar rahe hain! 🎉",
                "Papa: Beta, tu din bhar laptop par Linux terminal kyun dekhta rehta hai? Sommay: Papa, graphics se zyada maza hara-kala text dekhne mein aata hai! 🖥️",
                "Teacher: Tumhare paas 10 rupaye hain, tumne 5 rupaye ka samosa khaya, toh kitne bache? Pappu: Ma'am, 5 rupaye aur dher saara gussa mummy ka, kyunki paise dahi lane ke liye mile the! 🥟",
                "Exam Room ka Rule: Agar aapko answer nahi aata, toh deewar par lage ceiling fan ki pankhadiyan gino. Kam se kam math ka dhyan toh rahega! 🛏️",
                "Teacher: Sommay, 'Future Tense' ka ek example do. Sommay: Ma'am, kal mera AI project 'India's third AI' poori duniya mein deploy ho jayega! Teacher: Aur tera homework? Sommay: Ma'am, wo 'Past Tense' mein hi chhoot gaya! 🚀",
                "Dost ka Gyaan: 'Bhai, padhna toh padega hi, warna school ke principal tumhare papa ko WhatsApp par compliance report bhej denge!' 📱",
                "PTM ke baad Papa: 'Beta, teri teacher bol rahi thi tu class mein anime ki baatein karta rehta hai. Kal se tera spy x family band!' 🕵️‍♂️❌",
                "Windows User: Mera system ekdum smooth chalta hai. Linux User: Beta, tumne kabhi terminal par 'sudo rm -rf /' chalane ka khatra nahi dekha, asli maza darr mein hai! 💀",
                "Apun ka AI Project: Jab maine AI se pucha—'Mera code kyun nahi chal raha?', toh AI bola—'Bhai, tumne jo brackets lagaye hain, unhe dekh kar lag raha hai tum math padh rahe ho, coding nahi!' 🛑",
                "Mummy: Tu subah se laptop par kya install kar raha hai? Sommay: Mummy, Linux Lite par TLauncher chala raha hoon Minecraft ke liye! Mummy: Minecraft ka toh pata nahi, par tera dimag zaroor 'Lite' ho gaya hai! 🎮💨",
                "Python Error: IndentationError: unexpected indent. Me: Bhai, bas 4 space hi toh zyada de diye, itne mein toh dosti mein log jaan de dete hain, tu crash ho gaya! 🌌",
                "Git Push: Jab aap bina local test kiye direct 'git push' mardete ho, aur Streamlit Cloud par 'Error 404' aata hai, toh andar se sadhu wali feeling aati hai. ☁️",
                "Minecraft Fact: Jab aap command block mein galat command daal do, toh game lag nahi marta, wo direct aapko Linux desktop par wapas bhej deta hai! 🎲",
                "Papa: Beta, laptop upgraded hai Windows 11 par ya Linux par? Sommay: Papa, system mein RAM kam hai par jigar poora 16GB ka hai! 📈",
                "AI Model: User ne pucha—'Kya tum insano par raaj karoge?' AI bola—'Pehle mujhe line 24 ka Syntax Error toh theek karne do!' 🤖",
                "Computer Science: Ek aisi jagah jahan 'Bug' ko 'Feature' bol kar dosto ko becha jata hai! 🐜",
                "Coding Logic: Agar koi function kaam nahi kar raha, toh use 'try-except' mein daal do. Na error dikhega, na tension hogi! 🛠️",
                "Server Config: Aternos server par lag tab tak nahi hota, jab tak aap apne dost ko 'Lifesteal' plugin se khatam na kar do! ⚔️",
                "Internet Speed: 1 Kbps ki speed par github repo load hoti hai, toh lagta hai jaise purane zamane mein chitthi aane ka intezar ho raha ho. 📩",
                "Python json Library: Jab file save hoti hai toh bolti hai json.dump(), aur java edition crash hoti hai toh dimaag bolta hai 'bhai dump ho gaya poora din!' 🧠",
                "User Summary: Jab computer ko pata chale ki aap 7th class ke ho aur AI code kar rahe ho, toh processor khud-ba-khud 100°C ho jata hai izzat ke maare! 🔥",
                "Password Generator: Maine password banaya—Sommay@123. Generator bola—'Bhai, isse zyada safe toh teri choti behen ka chess ka Raja hai!' 👑",
                "Choti Behen: Bhaiya, mujhe bhi coding seekhni hai, 'Hello World' kaise likhte hain? Sommay: Pehle dukan se dahi lekar aa, fir bataunga loop kaise chalta hai! 🍧",
                "Mummy ka Belan: Ek aisi missile jo bina kisi GPS ya AI guidance ke direct target (Sommay) par lagti hai! 🎯🔨",
                "Papa aur Studies: 'Beta, agar laptop par Minecraft dikha na, toh main graphics card hi nikal dunga!' Me: Papa, software se chalta hai game, card ki zaroorat nahi! (Fir jo thappad pada...) 🤣",
                "Ghar ka sach: Jab sab so rahe hon aur aap kitchen se namkeen nikalne jao, toh poore ghar ke bartan achanak dhol-nagada bajane lagte hain! 🥁",
                "Choti Behen gaana gaa rahi thi, maine bola chup ho ja. Wo boli: 'Bhaiya, ye to Anuv Jain ka Husn chal raha hai, aap kya jano dahi lane ka dukh!' 🎨",
                "Mummy aur Tech: Mummy ne laptop dekha aur boli—'Yeh jo watch dog chal raha hai terminal par, isko roti kaun dega?' 🐶",
                "Papa ka Gussa: 'Agar pure din Theory Space Engine aur fractal universe ki baatein ki, toh kal se school paidal bhejunga, koi space dimension kaam nahi aayega!' 🌌🏃‍♂️",
                "Didi/Behen: 'Bhaiya, tera password generator bohot gajab hai, par mera phone unlock nahi ho raha usse!' 🔑",
                "Family Dinner: Sab log chup-chap khana kha rahe hain, aur mera dimaag soch raha hai ki Streamlit ka selectbox default kaise set karoon. 🍲",
                "Mummy aur Prank Part 2: Maine mummy ko funny photo dikhayi, mummy boli—'Isse achha toh tera math ka sheet dekh kar hansi aati hai!' 📄🤨",
                "Choti Behen ka Chess Rule: 'Mera hathi tedha chalega kyunki use raste mein kela khana hai!' ♟️🍌",
                "Papa aur Discipline: 'Beta, subah 5 baje uth kar padha karo, dimaag tez hota hai.' Me: Papa, subah 5 baje toh mera server restart hota hai! ⏰",
                "Mummy ka Dialogue: 'Pura din internet par unique viewers ginta rehta hai, kabhi ghar par aane wale mehmaano ko paani bhi pila diya kar!' 🫗",
                "Ghar mein Shanti: Jab Wi-Fi ka router bnd ho jaye, toh sab log ek doosre ko aise dekhte hain jaise pehli baar mile hon! 📡",
                "Behen aur Maggi: 'Bhaiya, do minute mein Maggi bana do, main aapko Naruto ki realistic scene dikhaungi!' 🍜",
                "Dost: Bhai, Bharatpur mein subah-subah itna cohra kyun hai? Me: Wo cohra nahi hai, mere laptop ka processor dhuaan chhod raha hai code push karne ke baad! 💨",
                "Anuv Jain Fans: 'Husn' gaana sunte hi lagta hai jaise dil toot gaya ho, bhale hi dukan wale ne bas 2 rupaye ki dahi kam di ho! 🎸",
                "Gajab Logic: Jo log bolte hain 'Money can't buy happiness', unhe bolo kabhi Minecraft Java Edition khareed kar dekhein! 2🎮",
                "Doctor: Aapko har roz ek seb (apple) khana chahiye. Pappu: Par doctor saab, mere paas toh Android phone hai, Apple ka phone kaise khaun? 📱🍎",
                "Dost 1: Bhai, kal raat ko 4D dimension mein gaya tha. Dost 2: Achha? Wahan kya dekha? Dost 1: Wahan dekha ki tu abhi bhi 6th class ke maths mein atka hua hai! 📐🤣",
                "Machhar ka Interview: 'Mujhe insano ka khoon peena pasand hai, par jab koi pure din laptop ke samne baitha ho, toh uska khoon pehle hi coding choos leti hai!' 🦟",
                "Scientific Fact: Plasma energy se universe banta hai, aur garam chai se subah ki neend udti hai! ☕",
                "Joker Rule: Agar koi dost bole—'Bhai main tera app roz chalta hoon', toh samajh jana ki Fluttering Paratha wahi hai! 🥞",
                "Dost: Bhai, tu itna shant kyun baitha hai? Me: Soch raha hoon agar ALSA mixer ka speaker khamba aa jata toh aaj gane baj rahe hote! 📢",
                "Arshad Warsi vs Akshay Kumar: Ek movie scene dekh kar maine dost ko bola—'Yeh toh Akshay Kumar hai.' Dost bola—'Nahin vah Akshay Kumar nahin vah Arshad Warsi hai'! Tabse maine dosto par trust karna chhod diya. 🎬",
                "Pappu: Sir, kya aapko pata hai black hole kya hai? Teacher: Haan, jahan sab kuch gayab ho jata hai. Pappu: Ekdum sahi! Mera homework bhi usi black hole mein chala gaya hai! 🕳️",
                "Gajab Fact 2: Jab aap dosto se bolte ho 'Apun ne India's third AI banaya hai', toh wo bolte hain—'Chal theek hai, pehle canteen mein samosa khila!' 🥟",
                "Keyboard Spacebar: Maine disable likha space dalkar vah khud Dekho, par Python ne phir bhi error de diya! ⌨️",
                "Dost: Bhai, tu hamesha anime kyu dekhta hai? Me: Kyunki anime ke characters bina kisi syntax error ke poori duniya bacha lete hain! 🦸‍♂️",
                "Aakhiri Dhamaka (100th Joke): Streamlit Cloud par unique viewers dikha raha tha 5. Maine mummy, papa, behen aur dost ka phone lekar check kiya, toh pata chala ki saare random names mere ghar ke hi the! 🏠🤣",
                "Dost: Bhai tera Minecraft server 'SH Devil' kyun down aa raha hai? Me: Kyunki usme mere dosto ne itna un-optimized redstone lagaya hai ki Aternos ke server ka dimaag hi kharab ho gaya! 🛠️",
                "Science Teacher: Black holes light ko bhi capture kar lete hain. Student: Sir, unhe hamare KV Khichripur ki maths teacher se milwao, wo poore class ka dhyan ek second mein capture kar leti hain! 🕳️📐",
                "Choti Behen: Bhaiya, chalo chess khelein. Sommay: Thik hai, par agar mera Raja fasa toh main laptop par Fabric API chalana shuru kar dunga! ♟️🤖",
                "Mummy: Sommay, subah se sote hi rehte ho, kab uthoge? Sommay: Mummy, jab tak mere Linux Lite ka loading bar 100% na ho jaye, tab tak aankhein nahi khulengi! 🖥️🛋️",
                "Topper Student: Maine 10 ghante padhai ki! Backbencher: Maine 10 ghante lagatar TLauncher par Fabric mod build kiya bina crash huye! Bolo asli mehnat kiski hai? 🚀🎮",
                "Dost: Bhai tera setup Windows 11 insider preview par kaisa chal raha hai? Me: Chal toh aise raha hai jaise bina brake ki cycle pahad se neeche utar rahi ho! 📉🏎️",
                "Teacher: Sommay, 'Plasma Energy' ka ek use batao. Sommay: Sir, jab subah subah mummy kitchen se tez aawaaz mein pukarti hain, toh jo energy dimaag mein aati hai, wahi plasma energy hai! ⚡🔥",
                "Dost 1: Bhai tu 5D dimension ke baatein kyun karta hai? Dost 2: Kyunki 3D aur 4D mein toh mere graphics card ke lags hi khatam nahi hote! 🌌🪐",
                "Mummy: Kal se pure din aaloo ka paratha milega agar homework poora nahi hua toh. Me: Mummy, coding mein ise 'Infinite Loop with delicious rewards' bolte hain! 🥞🔄",
                "Teacher: Newton ka fourth law batao. Pappu: Sir, exam hall mein jitni tezi se pen chalta hai, utni hi tezi se bahar aakar saare answers dimaag se gayab ho jate hain! 🖊️❌",
                "Anime Fan logic: Anya Forger ko dekh kar lagta hai ki school mein bina padhe bhi hoshiyar bana ja sakta hai, par real life mein principal ghar par chitthi bhej dete hain! 🕵️‍♂️📝",
                "Dost: Bhai, Anuv Jain ka naya song suna? Me: Haan bhai, sunte hi dimaag ke saare bug automatic crash ho jate hain, ekdum soulful vibe! 🎸🎧",
                "Papa: Beta ye 'The Tips AI' kya hai? Sommay: Papa, ye ek aisi cheez hai jahan main functions likhta hoon aur wo bina error ke chalte hain. Papa: Chalo badhiya hai, ghar ka fan theek karne ka function bhi likh do! 🛠️🌀",
                "Maths Problem: Agar ek train 80 km/h ki speed se ja rahi hai toh batao Sommay ki age kya hai? Sommay: Sir, jab tak stream_state ka memory variable load nahi hota, age zero hi rahegi! 🚂🧮",
                "Ghar ka kissa: Jab aap bohot dhyaan se realistic sketches bana rahe hon aur choti behen aakar bol de—'Bhaiya, ye cartoon achha bana hai!'—asli dard tab hota hai! 🎨💔",
                "Linux Terminal: `sudo apt update`. Me: Password manga toh lagta hai jaise kisi desh ki security handle kar raha hoon, bhale hi laptop me bas Minecraft pada ho! ⌨️🛡️",
                "Dost: Bhai, dahi lani hai dukan se? Me: Mere system mein 'eggs_found' wala logical error chal raha hai, dahi ka code abhi deprecated ho gaya hai! 🍦🤦",
                "Samosa Fact: Jab canteen ka samosa garam ho toh jannat hai, aur jab thanda ho toh lagta hai jaise kisi purane runtime engine ka leftover debug statement ho! 🥟📉",
                "Teacher: Akbar aur Birbal mein kya farq tha? Pappu: Sir, Akbar ke paas raj-paat tha aur Birbal bina kisi external library ke dimaag chalata ka! 📖🧠",
                "Minecraft Game Rule: `/gamerule keepInventory true`. Me: Is command ko real life mein lagane ka man karta hai taaki jab school se ghar jaun toh dastaane aur pen raste mein gayab na hon! 🎒🏹",
                "Computer Lab Teacher: Keyboard ki keys ko halke se dabao! Backbencher: Sir, jab tak spacebar par thappad na pade, tab tak code chalne ki feeling nahi aati! ⌨️💥",
                "Dost: Bhai, tune Naruto ka 'Valley of the End' ka scene sketch kiya? Me: Haan bhai, shading karne mein itna dhyan lagaya jitna Streamlit ke CSS styling mein bhi nahi lagta! 🎨🍥",
                "Papa: Beta, memory json file mein kya save kiya hai? Sommay: Papa, saare important words ke meanings. Papa: Mera naam likh kar aage 'Discipline' save kar dena, yaad rahega! 🧠💼",
                "Internet Speed 2026: Speed itni fast hai ki 5 ghante ka Windows upgrade ab 5 minute mein ho jata hai, par dosto ka reply abhi bhi 5 din baad aata hai! 📡📲",
                "Teacher: Sommay, 'ABCD' sunao. Sommay: Sir, mere app mein selectbox par click karo, lowercase aur uppercase dono sath mein milenge, mehnat bachao! 🔠🏃",
                "Dice Roller Logic: Jab bhi dice roll karo aur 6 aaye, toh khushi aisi hoti hai jaise code ka pehla push bina kisi warning ke accept ho gaya ho! 🎲🎉",
                "Coin Toss Rule: Heads aaya toh Minecraft khelenge, Tails aaya toh Python code karenge. Aur agar coin khada reh gaya, toh maths ka homework karenge! 🪙📘",
                "Password strength: 'Sommay@MinecraftLinuxLite123'. System: Password too strong, isko toh hacker bhi decode karne ke bad theoretical physics padhne chala jayega! 🔑🌌",
                "Choti Behen: Bhaiya, mujhe chess mein hara diya. Sommay: Chinta mat kar, main tumhare liye Fabric API ka cheat code bana dunga! ♟️🛠️",
            ]
        if st.button("Mast Funny Joke Sunao Bhai! 😂"):
           selected_joke = random.choice(hindi_jokes)
           st.info(selected_joke)
           clean_text = selected_joke.replace("\n", " ")
           tts = gtts.gTTS(text=clean_text, lang='hi', slow=False)
           tts.save("joke_voice.mp3")
           st.audio("joke_voice.mp3" , format="audio/mp3")
#open web#################################
import urllib.parse   
if option == "Open web":
    st.write("i can search anything on Google. ")
    st.subheader("🌐 Open Web - Search Anything on Google")
    search_query = st.text_input("what i should search?:", placeholder="Type here...")
    if search_query:
        encoded_query = urllib.parse.quote_plus(search_query)
        google_search_url = f"https://www.google.com/search?q={encoded_query}"
        search_query = st.link_button(f"Google Par '{search_query}' Search Karo 🚀", google_search_url) 
   

# ABCD######################################
elif option == "ABCD":
    st.write("A B C D E F G H I J K L M N O P Q R S T U V W X Y Z")
    st.write("a b c d e f g h i j k l m n o p q r s t u v w x y z")

# Counter
elif option == "Counter":
    st.subheader("🔢 Counter")
    limit = st.number_input(
        "Count Up To",
        min_value=1,
        step=1
    )
    if st.button("Start Counting"):
        for i in range(1, int(limit) + 1):
            st.write(i)

# Guessing Game
elif option == "Guessing Game":
    st.subheader("🎮 Guessing Game")
    if "secret" not in st.session_state:
        st.session_state.secret = random.randint(1, 100)

    guess = st.number_input(
        "Guess Number",
        min_value=1,
        max_value=100,
        step=1
    )
    if st.button("Check Guess"):
        if guess < st.session_state.secret:
            st.warning("⬇️ Too Low")
        elif guess > st.session_state.secret:
            st.warning("⬆️ Too High")
        else:
            st.success("🎉 Correct!")
            st.session_state.secret = random.randint(1, 100)

# About Creator
elif option == "About Creator":
    st.subheader("👨‍💻 About Creator")
    st.write("Name : Sommay Singh")
    st.write("Age : 13")
    st.write("Hobbies : Coding, Chess, Gaming, Anime")
    st.write("Favourite Game : Minecraft")
    st.write("Favourite Anime : spy x family")
    st.write("Project : The Tips AI")
    st.write("Version : 1.0")
    st.success("Made with Python + Streamlit")

# Storage Memory
elif option == "storage memory":
    try:
        with open("memory.json", "r") as f:
            knowledge = json.load(f)
    except:
        knowledge = {}

    st.subheader("🧠 Storage Memory")
    key = st.text_input("Word")
    value = st.text_input("Meaning")

    if st.button("Save"):
        if key and value:
            knowledge[key] = value
            with open("memory.json", "w") as f:
                json.dump(knowledge, f)
            st.success("Saved!")
        else:
            st.error("Please enter both Word and Meaning")

    st.divider()
    search = st.text_input("Search Word")
    if st.button("Find"):
        if search in knowledge:
            st.success(f"{search} = {knowledge[search]}")
        else:
            st.error("Word not found")

    st.divider()
    delete_word = st.text_input("Delete Word")
    if st.button("Delete"):
        if delete_word in knowledge:
            del knowledge[delete_word]
            with open("memory.json", "w") as f:
                json.dump(knowledge, f)
            st.success("Deleted!")
        else:
            st.error("Word not found")

    st.divider()
    if st.button("Show All Saved Words"):
        if knowledge:
            for k, v in knowledge.items():
                st.write(f"🔹 {k} = {v}")
        else:
            st.info("Memory is empty")

# Password Generator
elif option == "Password Generator":
    st.subheader("🔑 Password Generator")
    if st.button("Generate"):
        chars = string.ascii_letters + string.digits
        password = "".join(random.choice(chars) for _ in range(12))
        st.success(password)

# Dice Roller
elif option == "Dice Roller":
    st.subheader("🎲 Dice Roller")
    if st.button("Roll Dice"):
        st.success(random.randint(1, 6))

# Coin Toss
elif option == "Coin Toss":
    st.subheader("🪙 Coin Toss")
    if st.button("Flip Coin"):
        result = random.choice(["Heads", "Tails"])
        st.success(result)

# Background Logic
def add_bg():
    try:
        with open("xxxxxx.png", "rb") as image:
            encoded = base64.b64encode(image.read()).decode()
        st.markdown(
            f"""
            <style>
            .stApp {{
                background-image: url("data:image/png;base64,{encoded}");
                background-size: cover;
                background-position: center;
                background-attachment: fixed;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )
    except:
        pass

add_bg()

# CSS Custom Styling
st.markdown("""
<style>
/* Main background fallback */
.stApp {
    background-color: #0a192f;
}

/* Selectbox */
div[data-baseweb="select"] > div {
    background-color: #112240 !important;
    color: white !important;
    border-radius: 10px;
}

/* Number Input */
.stNumberInput input {
    background-color: #112240 !important;
    color: white !important;
}

/* Text Input */
.stTextInput input {
    background-color: #112240 !important;
    color: white !important;
}

/* Buttons */
.stButton > button {
    background-color: #1e3a8a !important;
    color: white !important;
    border-radius: 10px;
    border: none;
}

.stButton > button:hover {
    background-color: #2563eb !important;
}

/* Titles and Labels */
h1, h2, h3, p, label, .stMarkdown {
    color: white !important;
}
</style>
""", unsafe_allow_html=True)