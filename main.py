import os
import time
import scanner
import brain

# Ollama ko background mein start karne ke liye
print("Checking AI Engine status...")
os.system("start /b ollama serve") 
time.sleep(5) 

def start_sentinel():
    print("\n" + "="*30)
    print("🛡️  SENTINELGHOST ACTIVE  🛡️")
    print("="*30)

    while True:
        try:
            # 1. Scanning Phase
            # APNE WIFI KI RANGE CHECK KARKE YAHAN UPDATE KAREIN (e.g., 192.168.0.1/24)
            ip_range = "10.29.244.0/24" 
            print(f"\n[1] Scanning {ip_range}...")
            
            devices = scanner.scan_network(ip_range)
            print(f"[*] Found {len(devices)} devices. Data saved to JSON.")

            # 2. AI Analysis Phase
            print("[2] Requesting AI Risk Analysis from Llama-3.2...")
            verdict = brain.analyze_threats()
            
            print("\n" + "-"*20)
            print("🤖 AI VERDICT:")
            print(verdict)
            # Naya Trigger Logic: Agar Intruder mile toh Honeypot start ho jaye
            if "Intruder" in verdict or "8/10" in verdict:
                print("\n🔥 ALERT: UNKNOWN DEVICE DETECTED! Deploying Honeypot...")
                import subprocess
                # Honeypot ko background mein start karne ke liye
                subprocess.Popen(["python", "honeypot.py"])
            print("-"*20)

            # 3. Gap between scans
            print("\n[Next scan in 2 minutes... Press Ctrl+C to stop]")
            time.sleep(120)

        except KeyboardInterrupt:
            print("\nSentinelGhost stopped by user.")
            break
        except Exception as e:
            print(f"⚠️ System Error: {e}")
            time.sleep(10)

if __name__ == "__main__":
    start_sentinel()