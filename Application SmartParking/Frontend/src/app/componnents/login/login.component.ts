import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup } from '@angular/forms';
import { Router } from '@angular/router';
import { AuthenticationService } from 'src/app/services/authentication.service';

@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  errorMessage: any;
  userFormGroupe!: FormGroup;

  constructor(private fb: FormBuilder,
    private router: Router,
    private authService: AuthenticationService) { }

  ngOnInit(): void {
    this.userFormGroupe = this.fb.group({
      username: this.fb.control(""),
      password: this.fb.control("")
    })
  }

  login() {
    let username = this.userFormGroupe.value.username;
    let password = this.userFormGroupe.value.password;
    this.authService.login(username, password).subscribe({
      next: () => {
        this.authService.authenticateUser(this.userFormGroupe).subscribe({
          next: () => {
            this.router.navigateByUrl("/parking");
          }
        });
      },
        error: (err) => {
          this.errorMessage = err;
        }
      });
  }

}
