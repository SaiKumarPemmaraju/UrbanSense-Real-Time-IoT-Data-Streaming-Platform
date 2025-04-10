# 🌆 UrbanSense: Real-Time IoT Data Streaming Platform

## 🚀 Introduction
UrbanSense is a cutting-edge, real-time data streaming platform designed to simulate Internet-of-Things (IoT) scenarios, illustrating state-of-the-art big-data infrastructure and analytics solutions. It demonstrates the complete lifecycle of IoT sensor data—from initial capture through real-time processing to advanced analytics and cloud storage.

The platform simulates a connected vehicle journey from Central London to Birmingham, generating continuous, realistic sensor data including vehicle telemetry, GPS data, weather conditions, traffic camera images, and emergency incident notifications, all processed in real-time.

## 🎯 Why UrbanSense?
- **Realistic IoT Simulation**: Emulates practical use-cases of IoT in urban mobility.
- **Instantaneous Analytics**: Offers actionable insights through real-time analytics, enabling smarter and quicker decisions.
- **Scalable and Robust Architecture**: Designed for seamless scalability and resilience against data surges.
- **Cloud-Native Integration**: Deep integration with AWS services, demonstrating modern cloud-native data solutions.

## 🛠️ Technology Stack

- **Programming Languages:** Python (for data simulation and real-time processing)
- **Real-Time Data Ingestion:** Apache Kafka with Zookeeper
- **Real-Time Data Processing:** Apache Spark Structured Streaming
- **Cloud Storage & Analytics:** AWS S3, AWS Glue, Amazon Athena, Amazon Redshift
- **Containerization:** Docker, Docker Compose
- **Visualization:** PowerBI, Looker, or customizable dashboards

## 🗃️ Project Architecture

UrbanSense architecture comprises multiple interconnected components ensuring a seamless data journey:
![Screenshot 2025-04-10 073752](https://github.com/user-attachments/assets/3572a769-1f9c-4482-8c36-a27892b14a34)

### Data Flow Explanation

#### 1. IoT Data Simulator
The simulator generates continuous streams of sensor data replicating an actual vehicle journey scenario, including:
- Vehicle telemetry (speed, fuel, engine status)
- GPS-based location tracking
- Weather condition updates
- Traffic camera images
- Emergency incident alerts

#### 2. Kafka Ingestion Layer
- Kafka efficiently manages the ingestion of massive, high-frequency data streams.
- Data is segmented into distinct Kafka topics for organized management and streamlined processing.

#### 3. Spark Streaming & Processing Layer
- Real-time ingestion of Kafka streams.
- Conducts data cleaning, transformation, aggregation, and real-time analytics.

#### 4. AWS Cloud Storage and Analytics Layer
- Data storage in AWS S3, forming a reliable and scalable data lake.
- AWS Glue creates and manages data catalogs for optimized query performance.
- Amazon Athena facilitates rapid querying for ad-hoc analysis.
- Amazon Redshift provides powerful warehousing capabilities enabling deeper analysis and BI integration.
-  <img src="https://github.com/user-attachments/assets/2f795b64-587b-49aa-bbbe-767f99b87cee" width="350" height="270">


## 🚦 Installation & Setup Guide

Follow these clear and simple installation steps to get UrbanSense running:

### Detailed Installation Steps:

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Launch Docker Containers**
   ```bash
   docker-compose up -d
   ```
   -  <img src="https://github.com/user-attachments/assets/fefa93de-eb06-44f0-9a26-3066a6f3f9d5" width="350" height="300">



4. **AWS Configuration**
   - Set up AWS services including S3, Glue, Athena, and Redshift.
   - Update configuration files with AWS credentials and resource endpoints.

6. **Run the Simulator**
   ```bash
   python main.py
   ```

## 📊 Results and Visualization

The processed data can be visualized effectively using PowerBI, Looker, or custom dashboards, allowing stakeholders to interactively explore and interpret analytics results for timely decision-making.

## 🎖️ Key Achievements
- Developed a complete, resilient, and highly scalable real-time IoT data streaming pipeline.
- Integrated leading open-source technologies with AWS cloud services seamlessly.
- Successfully demonstrated comprehensive data handling from generation to actionable insights.

## 🌟 Future Roadmap
- Enhance analytics capabilities by integrating advanced predictive analytics and machine learning.
- Expand data accuracy and realism with real-time external API data integration.
- Create interactive visualization dashboards to enhance user experience and insight accessibility.

## 👤 About Me
I'm a dedicated Data Engineer passionate about crafting innovative, impactful, and data-centric solutions. Connect with me for collaborations or professional opportunities!

🌟 **Together, let’s innovate smarter cities!** 🌟

