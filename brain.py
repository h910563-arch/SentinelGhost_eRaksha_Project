import ollama
import json
 
# Yahan apne phone/laptop ke MAC addresses dalo (ipconfig /all se dekh kar)
TRUSTED_DEVICES = ["02:70:b0:a1:02:75"] 

def analyze_threats():
    try:
        with open("network_log.json", "r") as f:
            devices = json.load(f)

        if not devices:
            return "NO DEVICES DETECTED"

        # AI ko hum 'System Instructions' de rahe hain
        prompt = f"""
        Act as a Cybersecurity AI 'Sentinel'. 
        Analyze these devices: {devices}.
        Trusted Devices List: {TRUSTED_DEVICES}.

        Task:
        1. Compare each device with the Trusted List.
        2. If matched, Score: 1/10 (Safe).
        3. If NOT matched, Score: 8/10 (Intruder) and explain why.
        4. Provide a final 'VERDICT' at the end.
        """
        
        response = ollama.chat(model='llama3.2', messages=[{'role': 'user', 'content': prompt}])
        return response['message']['content']
    
    except Exception as e:
        return f"AI Error: {e}"