import subprocess
import time


def test_time_python(file, size):

    start_time = time.perf_counter()
    subprocess.call("python3 {} {}".format(file, size))
    stop_time = time.perf_counter()
    print("The file {} with a n-size of {} took {} seconds to compute".format(file, size, stop_time-start_time))

    #Write results to file
    fl = open("performance_test.txt", "a")
    fl.write("{};{};{}\n".format(file, size, stop_time-start_time))
    fl.close()

def test_time_cpp_release(file, size):

    start_time = time.perf_counter()
    subprocess.call("{} {}".format(file, size))
    stop_time = time.perf_counter()
    print("The file {} with a n-size of {} took {} seconds to compute".format(file, size, stop_time-start_time))

    #Write results to file
    fl = open("performance_test.txt", "a")
    fl.write("{};{};{}\n".format(file, size, stop_time-start_time))
    fl.close()

def test_time_cpp_debug(file, size):

    start_time = time.perf_counter()
    subprocess.call("{} {}".format(file, size))
    stop_time = time.perf_counter()
    print("The file {} with a n-size of {} took {} seconds to compute".format(file, size, stop_time-start_time))

    #Write results to file
    fl = open("performance_test.txt", "a")
    fl.write("{};{};{}\n".format(file, size, stop_time-start_time))
    fl.close()





if __name__ == "__main__":
    fl = open("performance_test.txt", "w")
    fl.close()
    test_time_python("nbody.py", 5000)
    test_time_cpp_debug("cmake-build-debug/nbody.exe", 5000)
    test_time_cpp_release("cmake-build-release/nbody.exe", 5000)
    test_time_python("nbody.py", 500000)
    test_time_cpp_debug("cmake-build-debug/nbody.exe", 500000)
    test_time_cpp_release("cmake-build-release/nbody.exe", 500000)
    test_time_python("nbody.py", 5000000)
    test_time_cpp_debug("cmake-build-debug/nbody.exe", 5000000)
    test_time_cpp_release("cmake-build-release/nbody.exe", 5000000)
    test_time_python("nbody.py", 50000000)
    test_time_cpp_debug("cmake-build-debug/nbody.exe", 50000000)
    test_time_cpp_release("cmake-build-release/nbody.exe", 50000000)

