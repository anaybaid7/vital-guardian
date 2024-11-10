# VitalGuardian - AI-Driven Health Monitoring System

Welcome to **VitalGuardian**! 🚀

In a world where healthcare access can be a challenge, especially in remote or underserved communities, **VitalGuardian** aims to bring health monitoring to the fingertips of those who need it most. Through an innovative integration of **Bluetooth-enabled wearable sensors**, **AI-powered health predictions**, and **real-time SMS alerts**, VitalGuardian is designed to empower individuals by providing proactive health insights without requiring constant supervision from medical professionals. 

## Features 🎉

- **Real-Time Health Monitoring**: Collects real-time data like heart rate, body temperature, blood oxygen levels from Bluetooth-enabled wearable sensors.
- **AI-Driven Predictions**: Uses a lightweight TensorFlow Lite model to predict health risks based on collected sensor data.
- **Instant Alerts**: Sends immediate SMS alerts via Twilio when health anomalies are detected, allowing for early intervention.
- **Offline Functionality**: Operates in areas with low or no internet connectivity by leveraging SMS notifications via Twilio.
- **Scalability**: Ideal for communities with multiple users, the system is built to scale and manage numerous devices at once.
- **Secure & Configurable**: Configuration files make it easy to set up Bluetooth devices and Twilio settings without touching the core code.

## Project Structure 🏗️

Here’s how the project is organized:

```bash
VitalGuardian/
├── src/                               # The heart of the system
│   ├── bluetooth_connector.py         # Manages Bluetooth connection and data collection
│   ├── health_predictor.py            # TensorFlow Lite prediction logic
│   ├── alert_sender.py                # Twilio integration for sending health alerts
│   └── main.py                        # Main execution script
├── models/                            # Where we store our machine learning models
│   └── health_model.tflite            # Pre-trained TensorFlow Lite model for health prediction
├── requirements.txt                  # Python dependencies required for the project
├── config/                            # Configuration files for Bluetooth and Twilio
│   ├── twilio_config.json             # Twilio API credentials and settings
│   └── bluetooth_config.json          # Bluetooth device configuration
├── utils/                             # Helpful utility scripts
│   ├── logger.py                      # Logging utility for system health tracking
│   └── data_preprocessor.py           # Data preprocessing for AI model input
└── README.md                          # Project documentation (this file)
