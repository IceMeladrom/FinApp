const ctx = document.getElementById('myChart');

var dict = {};
for (let i = 0; i < transaction_dates.length; i++) {
    let temp = new Date(transaction_dates[i][1]);
    temp = temp.getFullYear().toString() + ':' + temp.getMonth().toString() + ':' + temp.getDate().toString() + ':' + temp.getHours().toString()
    dict[temp] = transaction_dates[i][0];
}
console.log(dict);

const myChart = new Chart(ctx, {
    type: 'line',
    data: {
        datasets: [{
            label: 'Деньги',
            data: dict,
            backgroundColor: [
                'rgba(133, 187, 101, 1)',
            ],
            borderColor: [
                'rgba(133, 187, 101, 1)',
            ],
            borderWidth: 3,
        }],
    }
});