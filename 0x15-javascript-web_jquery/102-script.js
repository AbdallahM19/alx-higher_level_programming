$(document).ready(function () {
  const url = 'https://www.fourtonfish.com/hellosalut/hello/?';
  $('INPUT#btn_translate').click(function () {
    const languagecode = $('INPUT#language_code').val();
    $.get(url + $.param({ lang: languagecode }), function (data) {
      $('DIV#hello').html(data.hello);
    });
  });
});
