#!/bin/bash

APP_URL="http://localhost:5000"
LOG_FILE="health_check.log"

echo "=============================="
echo "Health Check Script"
echo "=============================="
echo "Checking app at: $APP_URL"
echo "Time: $(date)"

response=$(curl -s -o /dev/null -w "%{http_code}" $APP_URL)

if [ $response -eq 200 ]
then
    echo "✅ App is running!! Status: $response"
    echo "$(date) - App is running - Status: $response" >> $LOG_FILE
else
    echo "❌ ALERT!! App is down!! Status: $response"
    echo "$(date) - ALERT!! App is DOWN - Status: $response" >> $LOG_FILE
fi

echo "=============================="