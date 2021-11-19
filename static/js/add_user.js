document.addEventListener('DOMContentLoaded',() => {
  const file_input = document.querySelector('#file-input')
  const fileReader = new FileReader();

  file_input.addEventListener('change', () => {
    const file =  file_input.files[0]
    fileReader.readAsText(file,'Shift-JIS')
  })

  fileReader.addEventListener('load',() => {
    const file_result = fileReader.result.split('\r\n')
    //先頭行をヘッダーとして格納
    const header = file_result[0].split(',');
    //先頭行を削除
    file_result.shift();

      // CSVから情報を取得
    const items = file_result.map(item => {
      let datas = item.split(',');
      let result = {};
      for (const index in datas) {
        let key = header[index];
        result[key] = datas[index];
      }
      return result;
    });
  })
})