class AssignmentSubmission:
    def __init__(self, student_name, student_id, Assignment_title, due_date):
        self.name = student_name
        self.id = student_id
        self._Assignment_title = Assignment_title
        self._due_date = due_date
        self.__is_submitted = True
        self.__grade = None
        self.__submitted_files = []

    def __validate_grade(self, score: float):
        if 0 <= score <= 100:
            return True
        else:
            return False

    def __check_submission_status(self):
        if self.__is_submitted:
            return True
        return False

    def __is_duplicate(self, filename):
        if filename in self.__submitted_files:
            return True
        return False

    def add_file(self, filename):
        if self.__is_duplicate(filename):
            print("--> [Warning] '" + filename + "' is already attached!")
        else:
            self.__submitted_files.append(filename)
            print(
                "--> [Success]", self.name,
                "attached '" + filename + "'. Total files:",
                len(self.__submitted_files)
            )

    def remove_file(self, filename):
        if self.__grade is not None:
            print(
                "--> [Warning]", self.name,
                "cannot remove files. Assignment already graded."
            )
        elif filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            print("--> [Success]", self.name, "removed '" + filename + "'.")
        else:
            print("--> [Error]", filename, "not found.")

    def assign_grade(self, score):
        if len(self.__submitted_files) == 0:
            print(
                "--> [Error] Cannot grade. No files submitted for",
                self.name + "."
            )
        elif self.__validate_grade(score):
            self.__grade = score
            print(
                "--> [Success] Grade", score,
                "officially assigned to", self.name + "."
            )
        else:
            print("--> [Error] Invalid grade.")

    def get_grade(self):
        if self.__grade is None:
            return "Not Graded"
        return f"{self.__grade:g}"

    def view_files(self):
        if len(self.__submitted_files) == 0:
            return "No files"
        return ", ".join(self.__submitted_files)

    def get_status_report(self):
        if len(self.__submitted_files) == 0:
            status = "Missing"
        else:
            status = f"Submitted ({len(self.__submitted_files)} files)"

        return (
            f"ID: {self.id} | Name: {self.name} | "
            f"Status: {status} | Grade: {self.get_grade()}"
        )


print("--- INITIALIZING DROPBOX FOR STUDENT ---")
student1 = AssignmentSubmission (student_name="Alex Gonzaga", student_id="pshs-1090-x", Assignment_title="CS-101", due_date="2026-10-01")
student2 = AssignmentSubmission (student_name="Adelle", student_id="pshs-1920-x", Assignment_title="CS-103", due_date="2026-10-01")
student3= AssignmentSubmission (student_name="Juan dela Cruz", student_id="pshs-1033-x", Assignment_title="CS-101", due_date="2026-10-01")
student4 = AssignmentSubmission (student_name="Maria Santos", student_id="pshs-1044-x", Assignment_title="CS-101", due_date="2026-10-01")
student5 = AssignmentSubmission (student_name="Jose Reyes", student_id="pshs-1055-x", Assignment_title="CS-101", due_date="2026-10-01")
print()

print("--- TEST SCENARIO 1: Mutiple files via list ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"juan's Files {student3.view_files()}\n")

print("--- TEST SCENARIO 4: REmoving File After Being Graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print()

print("--- TEST SCENARIO 5: Empty list Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print()

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report()) 
print(student5.get_status_report())