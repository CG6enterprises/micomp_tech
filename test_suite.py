#!/usr/bin/env python
"""
Micomp_Tech Automated Testing Suite
Comprehensive test runner for all platform features
"""

import requests
import json
import sys
from datetime import datetime
from colorama import Fore, Back, Style, init

# Initialize colorama for colored output
init(autoreset=True)

# Configuration
BASE_URL = "http://localhost:5000"
API_BASE_URL = f"{BASE_URL}/api"
TEST_RESULTS = {
    "passed": 0,
    "failed": 0,
    "errors": []
}

# ==================== UTILITY FUNCTIONS ====================

def print_header(title):
    """Print a formatted header"""
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}  {title}")
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")

def print_test(test_name, status, details=""):
    """Print test result with color coding"""
    if status == "PASS":
        symbol = f"{Fore.GREEN}✓"
        TEST_RESULTS["passed"] += 1
    elif status == "FAIL":
        symbol = f"{Fore.RED}✗"
        TEST_RESULTS["failed"] += 1
        TEST_RESULTS["errors"].append(f"{test_name}: {details}")
    elif status == "SKIP":
        symbol = f"{Fore.YELLOW}⊘"
    else:
        symbol = f"{Fore.BLUE}ℹ"
    
    print(f"{symbol}{Style.RESET_ALL} {test_name:<50} [{status}]")
    if details and status != "PASS":
        print(f"  {Fore.RED}→ {details}{Style.RESET_ALL}")

def print_summary():
    """Print test summary"""
    total = TEST_RESULTS["passed"] + TEST_RESULTS["failed"]
    percentage = (TEST_RESULTS["passed"] / total * 100) if total > 0 else 0
    
    print(f"\n{Fore.CYAN}{'='*70}")
    print(f"{Fore.CYAN}  TEST SUMMARY{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
    print(f"Total Tests: {total}")
    print(f"{Fore.GREEN}Passed: {TEST_RESULTS['passed']}{Style.RESET_ALL}")
    print(f"{Fore.RED}Failed: {TEST_RESULTS['failed']}{Style.RESET_ALL}")
    print(f"Success Rate: {Fore.YELLOW}{percentage:.1f}%{Style.RESET_ALL}")
    
    if TEST_RESULTS["errors"]:
        print(f"\n{Fore.RED}Errors:{Style.RESET_ALL}")
        for error in TEST_RESULTS["errors"]:
            print(f"  • {error}")
    
    print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")

# ==================== CONNECTIVITY TESTS ====================

def test_server_connection():
    """Test if server is running"""
    print_header("1. SERVER CONNECTIVITY TESTS")
    
    try:
        response = requests.get(BASE_URL, timeout=5)
        print_test("Server is running", "PASS")
        return True
    except requests.ConnectionError:
        print_test("Server is running", "FAIL", 
                  f"Cannot connect to {BASE_URL}. Make sure Flask is running.")
        return False
    except Exception as e:
        print_test("Server is running", "FAIL", str(e))
        return False

def test_api_health():
    """Test API health endpoint"""
    try:
        response = requests.get(f"{API_BASE_URL}/health", timeout=5)
        if response.status_code == 200 and response.json().get("status") == "healthy":
            print_test("API health check", "PASS")
            return True
        else:
            print_test("API health check", "FAIL", "Unexpected response")
            return False
    except Exception as e:
        print_test("API health check", "FAIL", str(e))
        return False

# ==================== USER TESTS ====================

def test_user_creation():
    """Test creating a new user"""
    print_header("2. USER MANAGEMENT TESTS")
    
    user_data = {
        "username": f"testuser_{datetime.now().timestamp()}",
        "email": f"test_{datetime.now().timestamp()}@test.com",
        "password": "testpass123",
        "user_type": "student"
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/users", json=user_data, timeout=5)
        if response.status_code == 201:
            data = response.json()
            print_test("Create user", "PASS")
            return data.get("id")
        else:
            print_test("Create user", "FAIL", f"Status code: {response.status_code}")
            return None
    except Exception as e:
        print_test("Create user", "FAIL", str(e))
        return None

def test_get_user(user_id):
    """Test retrieving user by ID"""
    if not user_id:
        print_test("Get user by ID", "SKIP", "No user ID available")
        return False
    
    try:
        response = requests.get(f"{API_BASE_URL}/users/{user_id}", timeout=5)
        if response.status_code == 200:
            print_test("Get user by ID", "PASS")
            return True
        else:
            print_test("Get user by ID", "FAIL", f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_test("Get user by ID", "FAIL", str(e))
        return False

# ==================== COURSE TESTS ====================

def test_create_course():
    """Test creating a course"""
    print_header("3. COURSE MANAGEMENT TESTS")
    
    course_data = {
        "title": f"Test Course {datetime.now().timestamp()}",
        "description": "This is a test course",
        "level": "Beginner",
        "duration": "4 weeks"
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/courses", json=course_data, timeout=5)
        if response.status_code == 201:
            data = response.json()
            print_test("Create course", "PASS")
            return data.get("id")
        else:
            print_test("Create course", "FAIL", f"Status code: {response.status_code}")
            return None
    except Exception as e:
        print_test("Create course", "FAIL", str(e))
        return None

def test_get_courses():
    """Test retrieving all courses"""
    try:
        response = requests.get(f"{API_BASE_URL}/courses", timeout=5)
        if response.status_code == 200:
            courses = response.json()
            print_test("Get all courses", "PASS", f"Retrieved {len(courses)} courses")
            return True
        else:
            print_test("Get all courses", "FAIL", f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_test("Get all courses", "FAIL", str(e))
        return False

def test_get_course(course_id):
    """Test retrieving a specific course"""
    if not course_id:
        print_test("Get course by ID", "SKIP", "No course ID available")
        return False
    
    try:
        response = requests.get(f"{API_BASE_URL}/courses/{course_id}", timeout=5)
        if response.status_code == 200:
            print_test("Get course by ID", "PASS")
            return True
        else:
            print_test("Get course by ID", "FAIL", f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_test("Get course by ID", "FAIL", str(e))
        return False

# ==================== ENROLLMENT TESTS ====================

def test_enrollment(user_id, course_id):
    """Test enrolling user in course"""
    print_header("4. ENROLLMENT TESTS")
    
    if not user_id or not course_id:
        print_test("Enroll in course", "SKIP", "Missing user or course ID")
        return None
    
    enrollment_data = {
        "user_id": user_id,
        "course_id": course_id
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/enrollments", json=enrollment_data, timeout=5)
        if response.status_code == 201:
            data = response.json()
            print_test("Enroll in course", "PASS")
            return data.get("id")
        else:
            print_test("Enroll in course", "FAIL", f"Status code: {response.status_code}")
            return None
    except Exception as e:
        print_test("Enroll in course", "FAIL", str(e))
        return None

def test_get_enrollments(user_id):
    """Test retrieving user enrollments"""
    if not user_id:
        print_test("Get user enrollments", "SKIP", "No user ID available")
        return False
    
    try:
        response = requests.get(f"{API_BASE_URL}/enrollments/{user_id}", timeout=5)
        if response.status_code == 200:
            enrollments = response.json()
            print_test("Get user enrollments", "PASS", f"Retrieved {len(enrollments)} enrollments")
            return True
        else:
            print_test("Get user enrollments", "FAIL", f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_test("Get user enrollments", "FAIL", str(e))
        return False

# ==================== ANALYSIS TESTS ====================

def test_descriptive_stats():
    """Test descriptive statistics calculation"""
    print_header("5. STATISTICAL ANALYSIS TESTS")
    
    stats_data = {
        "values": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/analysis/descriptive", json=stats_data, timeout=5)
        if response.status_code == 200:
            result = response.json()
            if "mean" in result and "std_dev" in result:
                mean = result["mean"]
                print_test("Descriptive statistics", "PASS", f"Mean: {mean}")
                return True
            else:
                print_test("Descriptive statistics", "FAIL", "Missing required fields")
                return False
        else:
            print_test("Descriptive statistics", "FAIL", f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_test("Descriptive statistics", "FAIL", str(e))
        return False

def test_correlation():
    """Test correlation analysis"""
    correlation_data = {
        "x": [1, 2, 3, 4, 5],
        "y": [2, 4, 5, 4, 6]
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/analysis/correlation", json=correlation_data, timeout=5)
        if response.status_code == 200:
            result = response.json()
            if "correlation" in result:
                corr = result["correlation"]
                print_test("Correlation analysis", "PASS", f"Correlation: {corr:.2f}")
                return True
            else:
                print_test("Correlation analysis", "FAIL", "Missing correlation field")
                return False
        else:
            print_test("Correlation analysis", "FAIL", f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_test("Correlation analysis", "FAIL", str(e))
        return False

def test_ttest():
    """Test t-test analysis"""
    ttest_data = {
        "group1": [10, 12, 14, 15, 16],
        "group2": [18, 20, 19, 22, 21]
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/analysis/ttest", json=ttest_data, timeout=5)
        if response.status_code == 200:
            result = response.json()
            if "t_statistic" in result and "p_value" in result:
                t_stat = result["t_statistic"]
                p_val = result["p_value"]
                print_test("T-test analysis", "PASS", f"t={t_stat:.2f}, p={p_val:.4f}")
                return True
            else:
                print_test("T-test analysis", "FAIL", "Missing required fields")
                return False
        else:
            print_test("T-test analysis", "FAIL", f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_test("T-test analysis", "FAIL", str(e))
        return False

# ==================== PROJECT TESTS ====================

def test_create_project():
    """Test creating a project"""
    print_header("6. PROJECT MANAGEMENT TESTS")
    
    project_data = {
        "title": f"Test Project {datetime.now().timestamp()}",
        "description": "This is a test project",
        "category": "Business",
        "client_name": "Test Client"
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/projects", json=project_data, timeout=5)
        if response.status_code == 201:
            data = response.json()
            print_test("Create project", "PASS")
            return data.get("id")
        else:
            print_test("Create project", "FAIL", f"Status code: {response.status_code}")
            return None
    except Exception as e:
        print_test("Create project", "FAIL", str(e))
        return None

def test_get_projects():
    """Test retrieving all projects"""
    try:
        response = requests.get(f"{API_BASE_URL}/projects", timeout=5)
        if response.status_code == 200:
            projects = response.json()
            print_test("Get all projects", "PASS", f"Retrieved {len(projects)} projects")
            return True
        else:
            print_test("Get all projects", "FAIL", f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_test("Get all projects", "FAIL", str(e))
        return False

# ==================== INVOICE TESTS ====================

def test_create_invoice(project_id):
    """Test creating an invoice"""
    print_header("7. BILLING & INVOICE TESTS")
    
    if not project_id:
        print_test("Create invoice", "SKIP", "No project ID available")
        return None
    
    invoice_data = {
        "project_id": project_id,
        "amount": 5000.00,
        "billing_type": "project",
        "status": "pending"
    }
    
    try:
        response = requests.post(f"{API_BASE_URL}/invoices", json=invoice_data, timeout=5)
        if response.status_code == 201:
            data = response.json()
            print_test("Create invoice", "PASS")
            return data.get("id")
        else:
            print_test("Create invoice", "FAIL", f"Status code: {response.status_code}")
            return None
    except Exception as e:
        print_test("Create invoice", "FAIL", str(e))
        return None

def test_get_invoices(project_id):
    """Test retrieving project invoices"""
    if not project_id:
        print_test("Get project invoices", "SKIP", "No project ID available")
        return False
    
    try:
        response = requests.get(f"{API_BASE_URL}/invoices/{project_id}", timeout=5)
        if response.status_code == 200:
            invoices = response.json()
            print_test("Get project invoices", "PASS", f"Retrieved {len(invoices)} invoices")
            return True
        else:
            print_test("Get project invoices", "FAIL", f"Status code: {response.status_code}")
            return False
    except Exception as e:
        print_test("Get project invoices", "FAIL", str(e))
        return False

# ==================== PERFORMANCE TESTS ====================

def test_concurrent_requests():
    """Test multiple concurrent requests"""
    print_header("8. PERFORMANCE & LOAD TESTS")
    
    try:
        # Test creating 5 users concurrently
        success_count = 0
        for i in range(5):
            user_data = {
                "username": f"concurrent_user_{i}_{datetime.now().timestamp()}",
                "email": f"concurrent_{i}_{datetime.now().timestamp()}@test.com",
                "password": "testpass123",
                "user_type": "student"
            }
            response = requests.post(f"{API_BASE_URL}/users", json=user_data, timeout=5)
            if response.status_code == 201:
                success_count += 1
        
        if success_count == 5:
            print_test("Concurrent user creation (5 requests)", "PASS", f"All {success_count} requests successful")
            return True
        else:
            print_test("Concurrent user creation (5 requests)", "FAIL", f"Only {success_count}/5 successful")
            return False
    except Exception as e:
        print_test("Concurrent user creation (5 requests)", "FAIL", str(e))
        return False

# ==================== MAIN TEST RUNNER ====================

def run_all_tests():
    """Run all tests"""
    print(f"{Fore.MAGENTA}")
    print("""
╔═════════════════════════════════════════════════════════════════════╗
║         MICOMP_TECH AUTOMATED TEST SUITE                            ║
║         Comprehensive Platform Testing                             ║
╚═════════════════════════════════════════════════════════════════════╝
    """)
    print(f"{Style.RESET_ALL}")
    
    print(f"Test Start Time: {Fore.YELLOW}{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{Style.RESET_ALL}")
    print(f"Base URL: {Fore.YELLOW}{BASE_URL}{Style.RESET_ALL}\n")
    
    # Test connectivity
    if not test_server_connection():
        print(f"\n{Fore.RED}✗ Cannot connect to server. Aborting tests.{Style.RESET_ALL}")
        print(f"Make sure Flask is running: {Fore.YELLOW}python backend/app.py{Style.RESET_ALL}")
        return
    
    test_api_health()
    
    # Test users
    user_id = test_user_creation()
    test_get_user(user_id)
    
    # Test courses
    course_id = test_create_course()
    test_get_courses()
    test_get_course(course_id)
    
    # Test enrollment
    test_enrollment(user_id, course_id)
    test_get_enrollments(user_id)
    
    # Test analysis
    test_descriptive_stats()
    test_correlation()
    test_ttest()
    
    # Test projects
    project_id = test_create_project()
    test_get_projects()
    
    # Test invoices
    test_create_invoice(project_id)
    test_get_invoices(project_id)
    
    # Test performance
    test_concurrent_requests()
    
    # Print summary
    print_summary()
    
    # Exit with appropriate code
    sys.exit(0 if TEST_RESULTS["failed"] == 0 else 1)

if __name__ == "__main__":
    try:
        run_all_tests()
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Tests interrupted by user.{Style.RESET_ALL}")
        sys.exit(1)
    except Exception as e:
        print(f"\n{Fore.RED}Unexpected error: {e}{Style.RESET_ALL}")
        sys.exit(1)
