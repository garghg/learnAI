# learnAI
This is a learning path generater that asks user to input what they would like to learn and leverages Llama 3.1, tor, selenium, and BeautifulSoup to generate a path from beginner to advanced.
<img width="1919" height="956" alt="learnAI" src="https://github.com/user-attachments/assets/caa0a2d3-55e4-4233-8aeb-5d514edb4d79" />

---
## Set Up
You may download and run the exe file [here](https://drive.google.com/uc?export=download&id=1xh3vvLsT94QRyeRpGx9KRMNZAMU0CUoj).  
_The exe file uses Google Chrome v138 or later. To run it, please ensure you have chrome v138 or above on your system._  
OR  
1.  **Clone repo**: `git clone https://github.com/garghg/learnAI.git`
2.  Enter the src directory 
3. **Create venv**: `python -m venv venv`
4. **Activate venv**: `venv\Scripts\activate`
5. **Install dependencies**: `pip install -r requirements.txt`  
    If you have issue with requirements.txt, please run the following:
   1. `pip install flask`
   2. `pip install huggingface_hub`
   3. `pip install beautifulsoup4`
   4. `pip install stem`
   5. `pip install selenium`
   6. `pip install selenium_stealth`
6. **Run project**: `python main.py`
7. **Deactivate venv**: `deactivate`



_Note: In model.py, replace HUGGING_FACE_API_KEY with your own key. For test purposes, it will generate a python learning path if you use it without a key._  

### Create and use your own API key
1. Create a Hugging Face Account
2. Follow the instructions [here](https://youtu.be/HXBQzucTITQ?t=44)
   OR
   1. From the dashboard, click on your profile picture
   2. Navigate to Access Tokens
   3. Click on Create New Token
   4. Select Token Type: Read
   5. Give the token a name and hit Create Token
   6. Copy your newly generated token
4. In `model.py`, replace `api_key=os.environ["HUGGING_FACE_API_KEY"]` with `api_key=[your own api key here]` 

_Note: It may take a few minutes to generate a path. There may be occasional inaccuracies by the models used._
