sswtest(){
	docker run -it --rm \
	-v $(pwd):/app/data_ex \
	-e mypath=$(pwd) \
	manologcode/sswtest \
	python app.py "$@"
}
sswtest-rmi(){
	docker rmi manologcode/sswtest
}

