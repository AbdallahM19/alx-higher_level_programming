$(document).ready(function () {
  $.get(
    'https://swapi-api.alx-tools.com/api/films/?format=json',
    function (data, status) {
      if (status === 'success') {
        for (const i in data.results) {
          $('ul#list_movies').append('<li>' + data.results[i].title + '</li>');
        }
      }
    }
  );
});
