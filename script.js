document.getElementById('attendanceForm').addEventListener('submit', function(event) {
    event.preventDefault();
    const totalClasses = document.getElementById('totalClasses').value;
    const attendedClasses = document.getElementById('attendedClasses').value;
    const resultDiv = document.getElementById('result');

    if (totalClasses && attendedClasses) {
        const percentage = (attendedClasses / totalClasses) * 100;
        let message = `Attendance percentage: ${percentage.toFixed(2)}%`;

        if (attendedClasses / totalClasses < 0.75) {
            let daysNeeded = 1;
            while ((attendedClasses + daysNeeded) / (totalClasses + daysNeeded) < 0.75) {
                daysNeeded++;
            }
            message += `<br>For safe attendance, you need to attend the next ${daysNeeded} days.`;
        } else {
            let daysCanTakeLeave = 0;
            while ((attendedClasses - daysCanTakeLeave) / (totalClasses - daysCanTakeLeave) >= 0.75) {
                daysCanTakeLeave++;
            }
            message += `<br>For safe attendance, you can take leave up to ${daysCanTakeLeave - 1} days.`;
        }

        resultDiv.innerHTML = message;
    } else {
        resultDiv.innerHTML = 'Please enter both total number of classes and number of classes attended.';
    }
});
