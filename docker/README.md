# Docker Edge Container Deployment
**Milestone:** M3: Decide and Act  
**Task:** Docker  
**Max Marks:** 4 Marks  
**Student Name:** Sai Sanjay R  
**Student ID:** S20  
**GitHub Link:** [https://github.com/SAISANJAYR/edge_ai_sai/tree/main/docker](https://github.com/SAISANJAYR/edge_ai_sai/tree/main/docker)  

---

## 1. Rubric Requirement
> **"I build and start the container from a cold boot and trigger the actuator"**

---

## 2. Container Architecture
Edge Dockerfile optimized for ARM64 with `/dev/video*` and `/dev/gpiochip*` device passthrough:
```bash
# Cold boot launch command
docker run --rm -d --device=/dev/video0 --device=/dev/gpiochip4 --net=host edge_ai_sai:latest
```
