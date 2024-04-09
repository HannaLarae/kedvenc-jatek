
        function loadData() {
            const data = [
                { name: 'Játék 1', points: 10 },
                { name: 'Játék 2', points: 20 },
                { name: 'Játék 3', points: 30 },
                { name: 'Játék 4', points: 40 },
                { name: 'Játék 5', points: 50 },
            ];

            const maxPoints = Math.max(...data.map(game => game.points));
            const minPoints = Math.min(...data.map(game => game.points));
            const avgPoints = data.reduce((sum, game) => sum + game.points, 0) / data.length;

            const maxGames = data.filter(game => game.points === maxPoints);
            const minGames = data.filter(game => game.points === minPoints);

            const maxPointsElement = document.getElementById('maxPoints');
            const minPointsElement = document.getElementById('minPoints');
            const avgPointsElement = document.getElementById('avgPoints');

            maxPointsElement.textContent = `Legtöbb pontot kapó játékok: ${maxGames.map(game => game.name).join(', ')} (${maxPoints} pont)`;
            minPointsElement.textContent = `Legkevesebb pontot kapó játékok: ${minGames.map(game => game.name).join(', ')} (${minPoints} pont)`;
            avgPointsElement.textContent = `Átlagpontszám: ${avgPoints.toFixed(2)} pont`;

            const targetPoints = parseInt(prompt('Adja meg a pontszámértéket:'));
            const gamesAboveTargetPoints = data.filter(game => game.points > targetPoints);

            const gamesAboveTargetPointsElement = document.getElementById('gamesAboveTargetPoints');
            gamesAboveTargetPointsElement.textContent = `Az ennél nagyobb pontszámot elérő játékok: ${gamesAboveTargetPoints.map(game => game.name).join(', ')} (${gamesAboveTargetPoints.map(game => game.points).join(', ')}) pont`;

            const gamesAboveTargetPointsFile = gamesAboveTargetPoints.map(game => `${game.name}: ${game.points}`).join('\n');
            const blob = new Blob([gamesAboveTargetPointsFile], { type: 'text/plain;charset=utf-8' });
            const url = URL.createObjectURL(blob);
            const link = document.createElement('a');
            link.href = url;
            link.download = 'játékok_pont.txt';
            link.click();
            URL.revokeObjectURL(url);
     onload="loadData()">
    Játékok pontszámai
    id="maxPoints"
    id="minPoints"
    id="avgPoints"
    id="gamesAboveTargetPoints
