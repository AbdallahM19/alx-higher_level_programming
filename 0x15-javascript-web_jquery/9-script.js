$(document).ready(function () {
  $.get(
    'https://hellosalut.stefanbohacek.dev/?lang=fr',
    function (data, status) {
      if (status === 'success') {
        $('div#hello').text(data.hello);
      }
    }
  );
});
