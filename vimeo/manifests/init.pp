class vimeo (
){
	file { 'log_parser_5xx':
		ensure 	=> present,
		path 	=> '/usr/local/bin/log_parser.py',
		source 	=> 'python_log_parser:///vimeo/log_parser.py',
		owner 	=> 'root',
		group 	=> 'root',
		mode 	=> '0700',
	}
}
	
