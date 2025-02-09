from config import COMMAND_PREFIX

commands = [
    "alive - बॉट का स्टेटस चेक करें",
    "menu - सभी उपलब्ध कमांड्स देखें",
    "help - सभी कमांड्स की जानकारी प्राप्त करें",
    "owner - बॉट के मालिक की जानकारी",
    "download <url> - किसी भी इंस्टाग्राम पोस्ट/रील्स को डाउनलोड करें",
    "storyseen on/off - ऑटो स्टोरी व्यूइंग चालू/बंद करें",
    "unfollow on/off - ऑटो अनफॉलो मोड चालू/बंद करें",
    "storylike on/off - ऑटो स्टोरी लाइकिंग चालू/बंद करें",
    "storyreply on/off - ऑटो स्टोरी रिप्लाई चालू/बंद करें",
    "storyreplymsg <message> - स्टोरी रिप्लाई का मैसेज सेट करें",
    "autotyping on/off - चैट में टाइपिंग इंडिकेटर दिखाएँ",
    "alwaysonline on/off - हमेशा ऑनलाइन दिखने का मोड",
    "blocklist - सभी ब्लॉक किए गए यूज़र्स की लिस्ट देखें",
    "autodp on/off - ऑटो प्रोफाइल पिक्चर चेंजिंग चालू/बंद करें",
    "repoststory on/off - ऑटो स्टोरी रीपोस्ट चालू/बंद करें",
    "autostatus <text> - ऑटो स्टेटस अपडेट करें",
    "autodm on/off - ऑटो डीएम रिप्लाई चालू/बंद करें",
    "install <GitHub link> - नए फीचर्स जोड़ें",
    "remove <cmd> - किसी कमांड को हटा दें",
    "groupmanager on/off - ग्रुप मैनेजर चालू/बंद करें",
    "fakeonline on/off - फेक ऑनलाइन/ऑफलाइन सिस्टम",
    "caption <photo> - फोटो के लिए AI कैप्शन जेनरेट करें",
    "hashtag <keyword> - इंस्टाग्राम के लिए ट्रेंडिंग हैशटैग खोजें",
    "stalkers - यह देखें कि कौन आपका प्रोफाइल सबसे ज़्यादा देख रहा है",
    "viewprofile <username> - किसी इंस्टाग्राम प्रोफाइल का डेटा देखें",
    "play <song name> - यूट्यूब से गाना डाउनलोड करें और वॉइस में भेजें",
    "video <video title> - यूट्यूब से वीडियो डाउनलोड करके भेजें",
    "sticker <name> - स्टिकर खोजें और भेजें",
    "invite - ग्रुप इनवाइट लिंक जेनरेट करें",
    "antilink on/off - ग्रुप में लिंक भेजने से रोकें",
    "groupinfo - ग्रुप की जानकारी देखें",
    "jid - ग्रुप या चैट का JID (Jabber ID) प्राप्त करें",
    "img <keyword> - Google से इमेज डाउनलोड करके भेजें",
]

def run(bot, message, args):
    menu_text = "📜 *मेनू - उपलब्ध कमांड्स:* \n\n" + "\n".join([f"🔹 `{COMMAND_PREFIX}{cmd}`" for cmd in commands])
    return menu_text
