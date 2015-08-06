import mysql.connector
import os
import time

from db_config import config

media_root = '../media/'

if __name__ == "__main__":
	cnx = mysql.connector.connect(**config)

	print("Starting video format conversion, Press CTRL+C to exit")
	while True:
		cursor = cnx.cursor(buffered=True)
		cursorU = cnx.cursor(buffered=True)
		cursor.execute("SELECT id, video, image from dilidili_dev_video WHERE status=4;")
		for (pk, video, image) in cursor:
			video_full_path = (media_root + video).replace('/', '\\')
			video_name = video + ".converted.mp4"
			video_full_name = (media_root + video_name).replace('/', '\\')
			try:
				if os.system("ffmpeg -i %s -b:v 584k %s" % (video_full_path, video_full_name)) == 0:
					cursorU.execute("UPDATE dilidili_dev_video SET video='%s', status=1 WHERE id=%u;" % (video_name, pk))
			except os.error:
				pass
		else:
			print("No new video added")
		cnx.commit()
		time.sleep(10)

