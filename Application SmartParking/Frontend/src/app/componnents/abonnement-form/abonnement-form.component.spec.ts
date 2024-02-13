import { ComponentFixture, TestBed } from '@angular/core/testing';

import { AbonnementFormComponent } from './abonnement-form.component';

describe('AbonnementFormComponent', () => {
  let component: AbonnementFormComponent;
  let fixture: ComponentFixture<AbonnementFormComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ AbonnementFormComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(AbonnementFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
