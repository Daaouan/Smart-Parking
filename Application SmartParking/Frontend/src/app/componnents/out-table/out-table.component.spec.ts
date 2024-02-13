import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OutTableComponent } from './out-table.component';

describe('OutTableComponent', () => {
  let component: OutTableComponent;
  let fixture: ComponentFixture<OutTableComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ OutTableComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(OutTableComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
