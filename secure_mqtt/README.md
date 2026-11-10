# Secure MQTT Broker Configuration
**Milestone:** M4: Monitor and Connect  
**Task:** Secure MQTT  
**Max Marks:** 3 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/secure_mqtt](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/secure_mqtt)  

---

## 1. Rubric Requirement
> **"I show the broker refuses no-password and works with password + TLS"**

---

## 2. Security Validation
1. **Unauthenticated Connection Attempt:** Broker returns `Connection Refused: not authorized (Error Code 5)`.
2. **Authenticated TLS Connection:** Connects securely over Port 8883 with certificate verification.
