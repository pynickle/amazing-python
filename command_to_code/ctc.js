function replace_command_to_code(command) {
	lst=command.split('\n');
	result='';
	for (i in lst) {
		i=lst[i]
		if (i.startsWith(">>> ")) {
			i=i.replace(/>>> /,"");
		} else if (i.startsWith('... ')) {
			i=i.replace(/... /,"");
		} else if (i=="...") {
			i='';
		} else if (i==">>>") {
			i='';
		}
		result=result+i+'\n';
	}
	return result;
}
window.onload = function () {
	var command = document.getElementById('input');
	command.addEventListener('input',function () {
		var code=replace_command_to_code(this.value);
		document.getElementById('out').innerHTML = code;
	});
}
/*console.log(replace_command_to_code(`
>>> import asyncio
>>> async def print_num(num):
...     print(num)
...
>>> loop=asyncio.get_event_loop()
>>> loop.run_until_complete(
...     asyncio.wait([
...         print_num(num)
...         for num in range(10)
...     ])
... )
`))*/