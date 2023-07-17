
const ctx = document.getElementById('myChart');

new Chart(ctx, {
  type: 'pie',
  data: {
    labels: [
      "IIT Bhubaneswar",
      "IIT Bombay",
      "IIT Mandi",
      "IIT Delhi",
      "IIT Indore",
      "IIT Jodhpur",
      "IIT Gandhinagar",
      "IIT Patna",
      "IIT Hyderabad",
      "IIT Goa",
      "IIT Jammu",
      "IIT Dharwad",
      "IIT Tirupati",
      "IIT Bhilai",
      "IIT Palakkad",
      "IIT Ropar",
      "IIT Guwahati",
      "IIT Roorkee",
      "IIT Kharagpur",
      "IIT Madras",
      "IIT (ISM) Dhanbad",
      "IIT Kanpur",
      "IIT (BHU) Varanasi"
    ],
    datasets: [
      {
        data: [
          476,
          1356,
          520,
          1209,
          480,
          550,
          370,
          733,
          595,
          157,
          280,
          310,
          244,
          243,
          200,
          430,
          952,
          1353,
          1869,
          1134,
          1125,
          1210,
          1589
        ],
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
      },
    },
    plugins: {
      title: {
        display: true,
        text: 'Seat Matrix 2023',
        position: 'bottom',
      },
      legend:{
        display:'true',
        position:'right',
      },
    },
  },
});
