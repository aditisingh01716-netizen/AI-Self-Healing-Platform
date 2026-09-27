# AI-Powered Software Reliability and Self-Healing Platform

An AI-powered software reliability platform that monitors system resources, detects abnormal behavior, analyzes software incidents, determines risk levels, and performs controlled automatic recovery.

---

## Project Overview

Modern software systems can experience failures because of excessive CPU usage, memory consumption, disk utilization, application errors, service failures, or abnormal system behavior.

This project provides an intelligent reliability platform that continuously monitors a software environment and combines monitoring, machine learning, incident analysis, and automated recovery.

The system can:

- Monitor CPU usage
- Monitor memory usage
- Monitor disk usage
- Monitor application logs
- Detect application errors
- Detect critical failures
- Detect abnormal system behavior using Machine Learning
- Calculate incident severity
- Determine risk levels
- Recommend recovery actions
- Automatically recover a controlled test service
- Verify whether recovery was successful
- Store incidents in a SQLite database
- Display system status through a web dashboard
- Simulate controlled failure scenarios
- Run automated software tests
- Run inside Docker

---

# Architecture

```text
                 USER / WEB DASHBOARD
                         |
                         v
                  FLASK APPLICATION
                         |
                         v
                SYSTEM MONITORING
             /          |          \
            /           |           \
          CPU         MEMORY       DISK
            \           |           /
             \          |          /
                      LOGS
                       |
                       v
                AI ANALYSIS ENGINE
                       |
              +--------+--------+
              |                 |
              v                 v
       ANOMALY DETECTION    INCIDENT ANALYSIS
              |                 |
              +--------+--------+
                       |
                       v
                  RISK ENGINE
                       |
          +------------+------------+
          |            |            |
         LOW        MEDIUM       HIGH/CRITICAL
          |            |            |
          v            v            v
       NO ACTION    MONITOR       RECOVERY
                                      |
                                      v
                              SELF-HEALING ENGINE
                                      |
                                      v
                                HEALTH CHECK
                                      |
                         +------------+------------+
                         |                         |
                      HEALTHY                  FAILED
                         |                         |
                         v                         v
                    RECOVERED                   ALERT
                         |
                         v
                 INCIDENT DATABASE
                         |
                         v
                    WEB DASHBOARD