sswtest(){
	docker run -it --rm \
	-v $(pwd):/app/data_ext \
	-e mypath=$(pwd) \
	manologcode/sswtest \
	python app.py "$@"
}
sswtest-rmi(){
	docker rmi manologcode/sswtest
}

