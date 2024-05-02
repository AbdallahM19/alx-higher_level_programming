$(document).ready(function () {
  const apiUrl = 'https://www.fourtonfish.com/hellosalut/hello/?';
  function fetchTranslation () {
    const languageCode = $('INPUT#language_code').val();
    $.get(apiUrl + $.param({ lang: languageCode }), function (data) {
      $('#hello').text(data.hello);
    });
  }
  $('INPUT#btn_translate').click(fetchTranslation);
  $('INPUT#language_code').keypress(function (event) {
    if (event.which === 13) {
      fetchTranslation();
    }
  });
});
