from abc import ABC, abstractmethod

class ReportGenerator(ABC):

    def generate_report(self):
        self.parse()
        self.validate()
        
        if self.requires_revalidation():
            self.revalidate()
            
        self.save()
        print("Report Generated Successfully!\n")

    @abstractmethod
    def parse(self):
        pass

    @abstractmethod
    def validate(self):
        pass

    def revalidate(self):
        pass

    @abstractmethod
    def save(self):
        pass

    def requires_revalidation(self):
        return False


class StandardReport(ReportGenerator):

    def parse(self):
        print("Parsing standard report data...")

    def validate(self):
        print("Validating standard report data...")

    def save(self):
        print("Saving standard report file...")



class SpecialReport(ReportGenerator):

    def parse(self):
        print("Parsing special report data...")

    def validate(self):
        print("Validating special report data...")

    def revalidate(self):
        print("Revalidating special report data...")

    def save(self):
        print("Saving special report file...")

    def requires_revalidation(self):
        return True



if __name__ == "__main__":

    print("Generating Standard Report:")
    standard = StandardReport()
    standard.generate_report()

    print("Generating Special Report:")
    special = SpecialReport()
    special.generate_report()
