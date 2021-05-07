const songTable = $("#songTable");
const songFormular = $("#songFormular");
const songInput = $("#songInput");
const tableBody = $("#tableBody");
const noSongsFound = $("#noSongsFound");

function populateTable(songs) {
    songs.forEach(song => {
        const tableRow = `<tr><td>${song.artist}</td><td>${song.song}</td></tr>`;
        tableBody.append(tableRow)
    });
}

function clearTable() {
    tableBody.empty();
}

songFormular.submit(function(event) {
    event.preventDefault();
    const song = songInput.val();
    $.post("/songs", { song: song }, function(data) {
        clearTable();
        if (data.songs && data.songs.length > 0) {
            populateTable(data.songs);
            noSongsFound.hide();
            songTable.show();
        } else {
            noSongsFound.show();
            songTable.hide();
        }

    }).fail(function(error) {
        console.log("Something went wrong...");
    });
});