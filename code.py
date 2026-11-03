import streamlit as st

# Page Configuration
st.set_page_config(page_title="Crazy Google Page Codes", page_icon="🌀", layout="centered")

st.title("🌀 Crazy Google Page Codes")
st.write("Welcome to the ultimate browser prank collection! Copy these bookmarklet codes and share them with your friends.")

# --- SECTION 1: HOW TO MAKE A BOOKMARKLET ---
st.header("🛠️ How to Use These Codes")
st.markdown("""
1. **Show your Bookmarks Bar:** Press `Ctrl + Shift + B` (Windows) or `Cmd + Shift + B` (Mac).
2. **Create a New Bookmark:** Right-click an empty space on your bookmarks bar and select **Add page...**
3. **Name It:** Give it a sneaky name like `Google HD Mode`.
4. **Paste the Code:** Copy one of the JavaScript codes below and paste it directly into the **URL / Address** field, then hit **Save**.
5. **Trigger the Prank:** Go to any website and click your new bookmark!
""")

st.divider()

# --- SECTION 2: THE UPSIDE-DOWN PRANK ---
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

# --- SECTION 3: SLOWER SPINNING PAGE ---
st.header("🌀 Prank 2: Slow-Motion Spinning Page")
st.write("Makes the entire page spin in a smooth, hypnotic circle over 8 seconds instead of spinning too fast to handle.")

slow_spin_js = """javascript:(function(){
    var css = 'body { animation: spin 8s infinite linear; } @keyframes spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }';
    var style = document.createElement('style');
    style.type = 'text/css';
    style.appendChild(document.createTextNode(css));
    document.head.appendChild(style);
    alert('🌀 Slow-motion spin activated!');
})();"""

st.code(slow_spin_js, language="javascript")

# --- SECTION 4: ALIVE & RUNNING AROUND ---
st.header("🐛 Prank 3: 'It's Alive!' (Scurrying Text & Items)")
st.write("Turns every paragraph, title, button, and image on the page into a living entity that wiggles and runs around.")

alive_js = """javascript:(function(){
    var css = 'p, h1, h2, h3, a, img, span, button { animation: scurry 0.4s infinite alternate ease-in-out; display: inline-block; } @keyframes scurry { 0% { transform: translate(0px, 0px) rotate(0deg); } 100% { transform: translate(12px, -8px) rotate(4deg); } }';
    var style = document.createElement('style');
    style.type = 'text/css';
    style.appendChild(document.createTextNode(css));
    document.head.appendChild(style);
    alert('🐛 The page is alive! Everything is running around!');
})();"""

st.code(alive_js, language="javascript")