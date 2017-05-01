/**
 * Created by stephenfox on 01/05/2017.
 */
var actvityRenderer = function (el) {
    var renderTo = el;
    function formatDate(date) {
        return moment(date).format("HH:mm:ss");
    }

    function activityDuration(start, end) {
        var mStart = moment(start);
        var mEnd = moment(end);
        return moment(mEnd.diff(mStart)).format("HH:mm:ss");
    }

    /**
     * Displays actvities in table, and registers a callback that will
     * pass the index of the row that has been selected.
     * @param activities: The activities to display in the table.
     * @param onClickCallback: Callback which will pass the index
     *  of the row that was selected.
     * */
    function displayInTable(activities, onClickCallback) {
        var activityTableHTML =
            "<table class='table table-hover' id='activityTable'>" +
            '<thead>' +
            '<tr>' +
            '<th>Username</th>' +
            '<th>Distance</th>' +
            '<th>Duration</th>' +
            '<th>Start - End</th>' +
            '</tr>' +
            '</thead>' +
            '<tbody>' +
            '</tbody>' +
            '</table>';
        $(renderTo).append(activityTableHTML);
        activities.forEach(function (activity) {
            $('#activityTable  > tbody').append(
                '<tr>' +
                '<td>' + activity.properties.owner.username + '</td>' +
                '<td>' + parseFloat(activity.properties.distance).toFixed(3) + '</td>' +
                '<td>' + activityDuration(activity.properties.start, activity.properties.end) + '</td>' +
                '<td>' + formatDate(activity.properties.start) + ' - ' + formatDate(activity.properties.end) + '</td>' +
                '</tr>'
            )
        });
        // Register onClick listeners for each row.
        $('#activityTable tr').click(function () {
            if (onClickCallback) {
                onClickCallback($(this).closest('tr').index());
            }
        });
    }

    /**
     * Displays an activity on a LeafletJS map.
     * @param map reference
     * @param activity The activity to display
     * */
    function displayOnMap(map, activity) {
        map.setView([
            activity.geometry.coordinates[0][1],
            activity.geometry.coordinates[0][0]
        ], 16);
        L.geoJson(activity).addTo(map);
    }
    return {
        displayInTable: displayInTable,
        displayOnMap: displayOnMap,
        formatDate: formatDate,
        activityDuration: activityDuration
    }
};