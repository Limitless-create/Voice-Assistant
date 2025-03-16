# Voice-Assistant
"Jarvis" is a Python voice assistant. It uses speech recognition to open websites, perform Google searches, and play local media. Voice commands activate actions, with audio feedback. It's a basic, functional voice control project.
**Jarvis: A Voice-Controlled Personal Assistant**

This Python project, "Jarvis," is a fundamental voice-activated personal assistant designed to streamline common tasks through speech recognition. It demonstrates the integration of several key technologies to create a hands-free interactive experience.

**Core Functionality:**

* **Voice Interaction:**
    * Jarvis activates upon hearing keywords like "Jarvis," "Hello," or "Hi," initiating a command listening phase.
    * It utilizes `speech_recognition` to transcribe spoken commands into text, enabling user interaction without manual input.
    * `pyttsx3` is employed for text-to-speech conversion, providing audio feedback and delivering search result summaries.
* **Web Automation:**
    * The assistant can open popular websites such as Google, YouTube, Facebook, and Instagram using voice commands, leveraging the `webbrowser` module.
    * It integrates Google search functionality, processing search queries, and retrieving the top search result.
    * `requests` and `BeautifulSoup` are used to scrape and parse Google's search results, extracting the title, description, and link of the first result.
    * The top search result information is spoken to the user, and the link opened in the users default browser.
* **Media Playback:**
    * Jarvis supports local media playback through user-defined libraries.
    * Users can create `musiclibary.py` and `partlibary.py` files, containing dictionaries that map song or clip names to their corresponding URLs.
    * Voice commands like "Play [song name]" or "Song [clip name]" trigger the playback of the specified media.

**Technical Highlights:**

* The project showcases the use of external libraries for speech recognition, text-to-speech, web scraping, and browser automation.
* It provides a basic framework for building more complex voice-controlled applications.
* Error handeling is included, to catch basic exceptions.

**Intended Use:**

Jarvis serves as a practical demonstration of voice assistant technology, providing a foundation for further development and customization. It offers a convenient way to perform web searches, access websites, and play media using voice commands.
