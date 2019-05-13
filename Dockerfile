FROM alpine:3.7
RUN apk --update --no-cache add vim py2-pip && pip install redis flask 
ADD redis-wrapper.py /redis-wrapper.py
CMD FLASK_APP=/redis-wrapper.py flask run -h 0.0.0.0
