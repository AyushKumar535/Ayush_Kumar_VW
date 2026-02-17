import time
from abc import ABC, abstractmethod
from datetime import datetime


def log_report(func):
    def wrapper(*args, **kwargs):
        print(f"[LOG] Report generation started at {datetime.now()}")
        result = func(*args, **kwargs)
        print(f"[LOG] Report generation completed at {datetime.now()}")
        return result
    return wrapper


def measure_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[TIME] Execution Time: {end - start:.4f} seconds")
        return result
    return wrapper


def validate_data(func):
    def wrapper(self, *args, **kwargs):
        if not self.data:
            raise ValueError("No data available to generate report!")
        return func(self, *args, **kwargs)
    return wrapper




class FileManager:
    def __init__(self, filename):
        self.filename = filename
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, "w")
        print("[INFO] File opened successfully.")
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        if self.file:
            self.file.close()
            print("[INFO] File closed successfully.")




class Report(ABC):
    def __init__(self, data):
        self.data = data

    @abstractmethod
    def generate(self):
        pass

    @log_report
    @measure_time
    @validate_data
    def save(self, filename):
        with FileManager(filename) as file:
            for line in self.generate():  
                file.write(line + "\n")




class TextReport(Report):
    def generate(self):
        for item in self.data:
            yield f"Item: {item}"   


class StructuredReport(Report):
    def generate(self):
        for i, item in enumerate(self.data, start=1):
            yield f"{i}. {item['name']} - {item['value']}"



if __name__ == "__main__":

    text_data = ["Apple", "Banana", "Cherry"]
    text_report = TextReport(text_data)
    text_report.save("text_report.txt")

    print("\n------------------------\n")

    structured_data = [
        {"name": "Revenue", "value": "1000$"},
        {"name": "Profit", "value": "300$"},
    ]

    structured_report = StructuredReport(structured_data)
    structured_report.save("structured_report.txt")
