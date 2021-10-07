function commentReplyToggle(parent_id){
  const row = document.getElementById(parent_id);
    if (row.classList.contains('hidden')){
      row.classList.remove('hidden');
    }else{
      row.classList.add('hidden');
    }
};
