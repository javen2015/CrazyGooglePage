import streamlit as st

# Page Configuration
st.set_page_config(page_title="Crazy Google Page Codes", page_icon="🌀", layout="centered")

st.title("🌀 Crazy Google Page Codes")
st.write("Welcome to the ultimate browser prank collection! Copy these bookmarklet codes and share them with your friends.")

# --- SECTION 1: HOW TO MAKE A BOOKMARKLET ---
with st.expander("🛠️ How to Use These Codes (Click to Open)", expanded=True):
    st.markdown("""
    1. **Show your Bookmarks Bar:** Press `Ctrl + Shift + B` (Windows) or `Cmd + Shift + B` (Mac/iPad).
    2. **Create a New Bookmark:** Right-click an empty space on your bookmarks bar and select **Add page...** (or bookmark any random page and edit it).
    3. **Name It:** Give it a sneaky name like `Google HD Mode` or `Dark Theme Plus`.
    4. **Paste the Code:** Copy one of the JavaScript codes below and paste it directly into the **URL / Address** field, then hit **Save**.
    5. **Trigger the Prank:** Go to any website and click your new bookmark!
    """)

st.divider()

# --- PRANK 1 ---
st.header("🙃 Prank 1: The Upside-Down Webpage")
st.write("Rotates the entire webpage 180 degrees. Click it again to flip it back!")

upside_down_js = """javascript:(function(){
    var currentTransform = document.body.style.transform;
    if (currentTransform === 'rotate(180deg)') {
        document.body.style.transform = '';
        alert('🌐 Webpage restored to normal!');
    } else {
        document.body.style.transform = 'rotate(180deg)';
        document.body.style.transformOrigin = 'center';
        alert('🙃 Upside-down mode activated!');
    }
})();"""
st.code(upside_down_js, language="javascript")

# --- PRANK 2 ---
st.header("🌀 Prank 2: Slow-Motion Spinning Page")
st.write("Makes the entire page spin in a smooth, hypnotic circle over 8 seconds.")

slow_spin_js = """javascript:(function(){
    var css = 'body { animation: spin 8s infinite linear; } @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }';
    var style = document.createElement('style');
    style.type = 'text/css';
    style.appendChild(document.createTextNode(css));
    document.head.appendChild(style);
    alert('🌀 Slow-motion spin activated!');
})();"""
st.code(slow_spin_js, language="javascript")

# --- PRANK 3 ---
st.header("🐛 Prank 3: True Roaming Scurry ('It's Alive!')")
st.write("Breaks all text, images, and buttons loose and forces them to genuinely dart and crawl randomly all over the screen.")

true_scurry_js = """javascript:(function(){
    var elements = document.querySelectorAll('p, h1, h2, h3, img, button, a');
    elements.forEach(function(el) {
        el.style.position = 'fixed';
        el.style.zIndex = '999999';
        el.style.left = Math.random() * (window.innerWidth - 100) + 'px';
        el.style.top = Math.random() * (window.innerHeight - 50) + 'px';
        
        setInterval(function() {
            let currentX = parseFloat(el.style.left) || 0;
            let currentY = parseFloat(el.style.top) || 0;
            
            currentX += (Math.random() * 30 - 15);
            currentY += (Math.random() * 30 - 15);
            
            if (currentX < 0) currentX = 10;
            if (currentX > window.innerWidth - 100) currentX = window.innerWidth - 100;
            if (currentY < 0) currentY = 10;
            if (currentY > window.innerHeight - 50) currentY = window.innerHeight - 50;
            
            el.style.left = currentX + 'px';
            el.style.top = currentY + 'px';
        }, 100);
    });
    alert('🐛 True crawling chaos activated! Everything is running away!');
})();"""
st.code(true_scurry_js, language="javascript")

# --- PRANK 4 ---
st.header("🥴 Prank 4: The 'Drunk Wave' Page")
st.write("Waves the entire webpage back and forth like it's having a sea-sickness episode.")

drunk_wave_js = """javascript:(function(){
    var css = 'body { animation: drunkWave 4s infinite ease-in-out; transform-origin: center; } @keyframes drunkWave { 0% { transform: rotate(0deg) skew(0deg); } 25% { transform: rotate(2deg) skew(5deg); } 50% { transform: rotate(0deg) skew(0deg); } 75% { transform: rotate(-2deg) skew(-5deg); } 100% { transform: rotate(0deg) skew(0deg); } }';
    var style = document.createElement('style');
    style.type = 'text/css';
    style.appendChild(document.createTextNode(css));
    document.head.appendChild(style);
    alert('🥴 The page drank too much. Everything is wavy!');
})();"""
st.code(drunk_wave_js, language="javascript")

# --- PRANK 5 ---
st.header("🔀 Prank 5: The Text Shredder")
st.write("Randomly scrambles every single letter on the page like a broken typewriter, making text unreadable.")

text_shredder_js = """javascript:(function(){
    function scramble(node) {
        if (node.nodeType === 3) {
            node.nodeValue = node.nodeValue.split('').sort(function(){ return 0.5 - Math.random(); }).join('');
        } else {
            for (var i = 0; i < node.childNodes.length; i++) {
                scramble(node.childNodes[i]);
            }
        }
    }
    scramble(document.body);
    alert('🔀 Text shredded! Good luck reading anything.');
})();"""
st.code(text_shredder_js, language="javascript")

# --- PRANK 6 ---
st.header("🔦 Prank 6: Midnight Flashlight Mode")
st.write("Plunges the webpage into total darkness, turning their mouse cursor or touch into a tiny illuminating spotlight.")

flashlight_js = """javascript:(function(){
    var div = document.createElement('div');
    div.style.position = 'fixed';
    div.style.top = '0';
    div.style.left = '0';
    div.style.width = '100vw';
    div.style.height = '100vh';
    div.style.pointerEvents = 'none';
    div.style.zIndex = '999999';
    div.style.background = 'radial-gradient(circle 120px at 50% 50%, transparent 0%, rgba(0,0,0,0.98) 100%)';
    document.body.appendChild(div);
    
    document.addEventListener('mousemove', function(e){
        div.style.background = 'radial-gradient(circle 120px at ' + e.clientX + 'px ' + e.clientY + 'px, transparent 0%, rgba(0,0,0,0.98) 100%)';
    });
    document.addEventListener('touchmove', function(e){
        if(e.touches.length > 0){
            var touch = e.touches[0];
            div.style.background = 'radial-gradient(circle 120px at ' + touch.clientX + 'px ' + touch.clientY + 'px, transparent 0%, rgba(0,0,0,0.98) 100%)';
        }
    });
    alert('🔦 Flashlight mode activated! It is pitch black.');
})();"""
st.code(flashlight_js, language="javascript")
