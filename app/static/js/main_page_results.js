var arr = {{ games|safe }};
function addResult(winner, loser, i) {
    resultTemp =
        '<div class="card">\n' +
        '   <div class="card-header" id="heading'+i+'">' +
        '       <h2 class="mb-0">' +
        '           <button class="btn btn-link" type="button" data-toggle="collapse" data-target="#collapse'+i+'" ' +
        '               aria-expanded="true" aria-controls="collapse'+i+'">' +
        '               <h2 class = "text">' + winner + ' beats ' + loser + '</h2>\n' +
        '           </button>' +
        '       </h2>' +
        '   </div>' +
        '   <div id="collapse'+i+'" class="collapse" aria-labelledby="heading'+i+'" data-parent="#accordionDisp">' +
        '       <div class="card-body">' +
        '           More details...' +
        '       </div>' +
        '   </div>' +
        '</div><br>';
    $(resultTemp).appendTo( "#Disp" );
}

var winner;
var loser;
for (var i = 0; i < {{numberOfGames}}; i = i + 1) {
    winner = arr[i][0];
    loser = arr[i][1];
    addResult(winner, loser, i);
}
