# ALX Grading System Outage Postmortem

## 📋 Issue Summary

- **Duration**: March 15, 2025, 14:30 UTC to March 16, 2025, 09:45 UTC (19 hours, 15 minutes)
- **Impact**: Student grades failed to update despite on-time assignment submissions
- **Severity**: Critical - 100% of grade update requests resulted in 500 errors
- **Root Cause**: Database lock contention between scheduled maintenance and high submission volume

## ⏱️ Timeline (UTC)

| Time                | Event                                                  |
| ------------------- | ------------------------------------------------------ |
| **March 15, 14:30** | Grading system began failing to update student grades  |
| **March 15, 16:45** | First student support tickets reported                 |
| **March 15, 17:30** | Engineering team notified via monitoring alerts        |
| **March 15, 18:15** | Initial investigation focused on frontend issues       |
| **March 15, 20:00** | Database team identified lock contention issue         |
| **March 15, 22:30** | Attempted to terminate maintenance job (unsuccessful)  |
| **March 16, 01:15** | Implemented temporary queue system workaround          |
| **March 16, 03:45** | Scaled up database to handle increased connection load |
| **March 16, 08:00** | Began processing backlog of grade updates              |
| **March 16, 09:45** | Service fully restored, all grades correctly reflected |

## 🔍 Root Cause

A quarterly database optimization job was scheduled during what was historically a low-traffic period but conflicted with a newly introduced project deadline for a large cohort. The optimization job acquired exclusive locks on key database tables, preventing the grading system from writing new grade records. As submission volume increased, database connection pools were exhausted by pending write operations, causing cascading failures.

## 🛠️ Resolution and Recovery

1. Attempted to force-terminate the maintenance job
2. Implemented temporary asynchronous queue system for grade submissions
3. Vertically scaled the database instance (doubled RAM and CPU)
4. Manually cleared problematic locks after identifying affected tables
5. Processed backlogged grade updates with rate limiting
6. Verified all student grades were correctly updated with original submission timestamps
7. Communicated to students that no submissions would be marked late due to the outage

## 🚀 Corrective and Preventative Measures

### Scheduling Improvements

- Create shared calendar for maintenance jobs with cross-team visibility
- Implement blackout periods during known high-traffic events
- Add assignment deadline information to infrastructure planning tools

### Technical Improvements

- Redesign database schema to reduce lock contention
- Implement permanent queue-based architecture for grade processing
- Add database connection pool monitoring with auto-scaling
- Create more granular database partitioning based on cohort activity

### Monitoring Enhancements

- Add specific monitoring for database lock contention metrics
- Implement early warning system for connection pool saturation
- Create dedicated dashboard for submission/grading pipeline health

### Process Improvements

- Establish cross-team review process for maintenance scheduling
- Update incident response playbook with database troubleshooting steps
- Conduct regular load testing simulating peak submission periods
- Institute reviews of application patterns that might create database contention

### Communication Plan

- Develop automated status page updates during outages
- Create templated communications for different types of grading issues
- Establish clearer escalation paths from student support to engineering

## 💬 Final Note

We sincerely apologize for the stress and inconvenience this outage caused our students. We understand the importance of reliable grading feedback and are committed to rebuilding trust through these improvements.
