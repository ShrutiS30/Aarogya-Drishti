SELECT 
    Activity_Segment,
    COUNT(*) AS Total_Records,
    AVG(Steps_Taken) AS Avg_Steps,
    AVG(Calories_Burned) AS Avg_Calories,
    AVG(Hours_Slept) AS Avg_Sleep,
    AVG(Stress_Level_1_10) AS Avg_Stress
FROM HealthPulse_Final_Data
GROUP BY Activity_Segment
ORDER BY Avg_Steps DESC;
--2--
SELECT 
    Month,
    COUNT(*) AS Total_Records,
    AVG(Steps_Taken) AS Avg_Steps,
    AVG(Calories_Burned) AS Avg_Calories,
    AVG(Hours_Slept) AS Avg_Sleep,
    AVG(Stress_Level_1_10) AS Avg_Stress
FROM HealthPulse_Final_Data
GROUP BY Month
ORDER BY 
    CASE Month
        WHEN 'January' THEN 1
        WHEN 'February' THEN 2
        WHEN 'March' THEN 3
        WHEN 'April' THEN 4
        WHEN 'May' THEN 5
        WHEN 'June' THEN 6
        WHEN 'July' THEN 7
        WHEN 'August' THEN 8
        WHEN 'September' THEN 9
        WHEN 'October' THEN 10
        WHEN 'November' THEN 11
        WHEN 'December' THEN 12
    END;

    --3--
    SELECT TOP 10
    User_ID,
    Full_Name,
    Date,
    Steps_Taken,
    Hours_Slept,
    Active_Minutes,
    Stress_Level_1_10,
    Activity_Segment
FROM HealthPulse_Final_Data
ORDER BY Stress_Level_1_10 DESC, Hours_Slept ASC;

--4--
SELECT 
    Stress_Level_1_10 AS Stress_Level,
    COUNT(*) AS Total_Records,
    AVG(Hours_Slept) AS Avg_Hours_Slept,
    AVG(Steps_Taken) AS Avg_Steps,
    AVG(Calories_Burned) AS Avg_Calories
FROM HealthPulse_Final_Data
GROUP BY Stress_Level_1_10
ORDER BY Stress_Level_1_10;

--5--
SELECT TOP 10
    User_ID,
    Full_Name,
    COUNT(*) AS Total_Days_Tracked,
    AVG(Steps_Taken) AS Avg_Daily_Steps,
    AVG(Calories_Burned) AS Avg_Daily_Calories,
    AVG(Hours_Slept) AS Avg_Sleep,
    AVG(Active_Minutes) AS Avg_Active_Minutes,
    AVG(Stress_Level_1_10) AS Avg_Stress
FROM HealthPulse_Final_Data
GROUP BY User_ID, Full_Name
ORDER BY Avg_Daily_Steps DESC;

--6--
SELECT 
    COUNT(*) AS Total_Records,
    COUNT(DISTINCT User_ID) AS Total_Users,
    AVG(Steps_Taken) AS Overall_Avg_Steps,
    AVG(Calories_Burned) AS Overall_Avg_Calories,
    AVG(Hours_Slept) AS Overall_Avg_Sleep,
    AVG(Active_Minutes) AS Overall_Avg_Active_Minutes,
    AVG(Stress_Level_1_10) AS Overall_Avg_Stress
FROM HealthPulse_Final_Data;

--7--
SELECT 
    Activity_Segment,
    COUNT(*) AS Total_Records,
    CAST(
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () 
        AS DECIMAL(5,2)
    ) AS Percentage
FROM HealthPulse_Final_Data
GROUP BY Activity_Segment
ORDER BY Total_Records DESC;